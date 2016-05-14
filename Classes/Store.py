from Classes.Menu import *
from Data.inventory import *


class Shop(Menu):
    def __init__(self, hero):
        Menu.__init__(self)
        self.unit = hero
        self.gold = hero.Gold
        self.menu = [
            {"left": " ", "right": " ", "name": WEAPONS[1]['label'], "price": WEAPONS[1]['price'], "lp": "{:<12}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[2]['label'], "price": WEAPONS[2]['price'], "lp": "{:<13}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[3]['label'], "price": WEAPONS[3]['price'], "lp": "{:<14}".format(' ')},
            {"left": " ", "right": " ", "name": 'Exit', "price": '', "lp": "{:<15}".format(' ')}
        ]
        self.line = {"left": ">", "right": "<", "name": WEAPONS[1]['label'], "price": WEAPONS[1]['price'], "lp": "  "}
        self.template_line = "|{line[left]}| {line[name]} {line[price]} {line[lp]} |{line[right]}|"
        self.selected_line = WEAPONS[1]['label']
        self.d = None

    def find(self):
        for d in self.menu:
            if d["name"] == self.selected_line:
                self.d = d

    def select(self):
        self.find()
        if self.selected_line == "Exit":
            return True
        elif self.selected_line == self.d["name"]:
            if self.gold > int(self.d["price"]) or self.gold == int(self.d["price"]):
                self.gold -= int(self.d["price"])
                Invent.weapon = WEAPONS[3]
                self.unit.Gold = self.gold
                print(self.gold)
            else:
                print(self.gold)
                print('not enouth Gold')

