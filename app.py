from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    response = {
        'message': 'Message received successfully!',
        'received_data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
