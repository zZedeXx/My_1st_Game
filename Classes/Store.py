from Classes.Menu import *
from Data.inventory import *


class Shop(Menu):
    def __init__(self, gold):
        Menu.__init__(self)
        self.gold = gold
        self.menu = [
            {"left": " ", "right": " ", "name": WEAPONS[1]['label'], "price": WEAPONS[1]['price'], "lp": "{:<12}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[2]['label'], "price": WEAPONS[2]['price'], "lp": "{:<13}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[3]['label'], "price": WEAPONS[3]['price'], "lp": "{:<14}".format(' ')},
            {"left": " ", "right": " ", "name": 'Exit', "price": '', "lp": "{:<15}".format(' ')}
        ]
        self.line = {"left": ">", "right": "<", "name": WEAPONS[1]['label'], "price": WEAPONS[1]['price'], "lp": "  "}
        self.template_line = "|{line[left]}| {line[name]} {line[price]} {line[lp]} |{line[right]}|"
        self.selected_line = WEAPONS[1]['label']

    def find(self):
        for d in self.menu:
            if d["name"] == self.selected_line:
                return d

    def select(self):
        if self.selected_line == "Exit":
            return True
        elif self.selected_line != "Exit":
            if self.gold > int(self.find()["price"]) or self.gold == int(self.find()["price"]):
                self.gold -= int(self.find()["price"])
                Invent.weapon = self.find()
            else:
                print('not enouth Gold')

