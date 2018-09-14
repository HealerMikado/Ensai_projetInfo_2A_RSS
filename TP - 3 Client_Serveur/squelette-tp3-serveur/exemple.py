from flask import Flask, request
import json

app = Flask(__name__)


movies = ['La Quatuor à Cornes', 'Thunder Road', 'Venom']


@app.route("/films", methods=['GET'])
def movieList():
    return json.dumps({"films": movies})


@app.route("/film", methods=['POST'])
def addMovie():
    content = request.get_json()
    movies.append(content['name'])
    return json.dumps({"result": "success"})


if __name__ == "__main__":
    app.run()
