
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi, this is Meyorm"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"key": "value"}  # Corrected this line
    return jsonify(data)

if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))


