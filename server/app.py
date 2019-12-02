import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from game.words import Game

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

game = Game()


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/start')
def start():
    game.start()
    return "Le jeu a commencé"


@app.route('/cards')
def get_cards():
    return jsonify(game.get_dict())


@app.route('/picked', methods=['POST'])
def picked():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    print("toto", post_data)
    game.cards[post_data["id"]]["picked"] = not(post_data["picked"])
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
