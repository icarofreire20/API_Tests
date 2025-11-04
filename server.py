from flask import Flask, jsonify, request
import datetime
import ssl

# Initialize Flask app
app = Flask(__name__)


@app.route('/hora', methods=['GET'])
def hora():
    now = datetime.datetime.now()
    return jsonify({"hora": now})


# Run the Flask app with SSL encryption
if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain('certs/server.crt', 'certs/server.key')
    context.load_verify_locations('certs/ca.crt')
    app.run(debug=True, host='0.0.0.0', port=8443, ssl_context=context)