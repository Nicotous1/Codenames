import random

import numpy as np
from typing import List, Set

import os

file_folder = os.path.dirname(os.path.abspath(__file__))
words_path = os.path.join(file_folder, "words.txt")

def get_words()->List[str]:
    f = open(words_path, "r", encoding="utf-8")
    words = []
    for l in f:
        if l[:4] == "Noms":
            line_words = l[7:].strip()#.replace(" ", "")
            words += line_words.split(",")
    words = extract_unique_values_of_list(words)
    f.close()
    return words

def extract_unique_values_of_list(words:List[str])->List[str]:
    return list(set(words))


def generate_colors():
    colors = np.array(["white"] * 25)

    random_picked = np.random.choice(25, 8 * 2 + 1, replace=False)
    # Set blue = 1
    colors[random_picked[:8]] = "blue"

    # Set red = 2
    colors[random_picked[8:16]] = "red"

    # Set black = 3
    colors[random_picked[16]] = "black"

    return colors


def generate_words():
    words = get_words()
    return np.random.choice(words, size=25, replace=False)


def generate_cards():
    words = generate_words()
    colors = generate_colors()

    cards = []

    for i, (word, color) in enumerate(zip(words, colors)):
        card = {"word": word,
                "color": color,
                "picked": True,
                "id": i
                }
        cards.append(card)
    return cards

class Game(object):

    def __init__(self):
        self.cards = None
        self.start()

    def start(self):
        self.cards = generate_cards()

    def pick(self, i, is_picked):
        self.cards[i]["picked"] = is_picked

    def get_score(self):
        scores = {}
        for card in self.cards:
            color = card["color"]
            if not(color in scores):
                scores[color] = {"N":0, "k":0}
            scores[color]["N"] += 1
            if not(card["picked"]):
                scores[color]["k"] += 1
        return scores

    def get_dict(self):
        game = {}
        game["cards"] = self.cards
        game["scores"] = self.get_score()
        return game




if __name__ == "__main__":
    print(generate_cards())
