import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():

    file = open("data.json", "r")
    
    data = json.load(file)
    
    file.close()
    
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
