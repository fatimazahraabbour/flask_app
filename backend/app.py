#to run the backend execute "flask run"
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, abbour!</p>"
@app.route("/signup",methods=["POST"])
def signup():
    return jsonify({
        "id":"1",
        "email":"fatimazahrabbour@gmai.com"
    })

if __name__ == "__main__":
    app.run(debug=True)