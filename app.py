from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/you', methods=['POST'])
def hello_world():
    request_json = request.get_json()
    return jsonify(greeting=f"hello {request_json['username']}")
