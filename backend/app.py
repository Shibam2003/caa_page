from flask import Flask, request, jsonify
import dns.resolver
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all cross-origin requests

# Use Google's public DNS resolver for better reliability
resolver = dns.resolver.Resolver()
resolver.nameservers = ['1.1.1.1']  # You can use other public DNS resolvers like Cloudflare (1.1.1.1)

@app.route('/query-caa', methods=['POST'])
def query_caa():
    try:
        # Get domain from the POST request body
        data = request.get_json()
        domain = data.get('domain', '').strip()

        if not domain:
            return jsonify({"error": "Domain name is required"}), 400

        # Query CAA records for the domain
        try:
            answers = resolver.resolve(domain, 'CAA')
            if not answers:
                return jsonify({"caaRecords": "No CAA records found."})

            # Process the CAA records
            caa_records = []
            for rdata in answers:
                record = {
                    "flag": rdata.flags.decode('utf-8') if isinstance(rdata.flags, bytes) else rdata.flags,
                    "tag": rdata.tag.decode('utf-8') if isinstance(rdata.tag, bytes) else rdata.tag,
                    "value": rdata.value.decode('utf-8') if isinstance(rdata.value, bytes) else rdata.value
                }
                caa_records.append(record)
            return jsonify({"caaRecords": caa_records})
        except dns.resolver.NoAnswer:
            return jsonify({"error": "No CAA records found."}), 404
        except dns.resolver.NXDOMAIN:
            return jsonify({"error": "Domain does not exist."}), 404
        except dns.resolver.YXDOMAIN:
            return jsonify({"error": "The domain name is invalid."}), 400
        except Exception as e:
            print(f"Backend error while querying CAA records: {str(e)}")
            return jsonify({"error": "Internal server error. Check backend logs."}), 500
    except Exception as e:
        print(f"Unexpected backend error: {str(e)}")
        return jsonify({"error": "Internal server error. Check backend logs."}), 500


if __name__ == '__main__':
    app.run(debug=True)
