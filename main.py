

from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return "Hi, this is Meyorm"
@app.route('/api/data',methods=['GET'])
def get_data():
    data= {"key","value"}
    return jsonify(data)
if __name__== '__main':
    app.run(debug=True)
