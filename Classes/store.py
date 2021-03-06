from Classes.menu import *
from Classes.inventory import *
from Data.inventory import inventar


class Shop(Menu):
    def __init__(self, hero):
        Menu.__init__(self)
        self.inv = Invent(hero, inventar)
        self.unit = hero
        self.menu = [
            {"left": " ", "right": " ", "name": WEAPONS[1]['name'], "price": WEAPONS[1]['price'], "lp": "{:<12}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[2]['name'], "price": WEAPONS[2]['price'], "lp": "{:<13}".format(' ')},
            {"left": " ", "right": " ", "name": WEAPONS[3]['name'], "price": WEAPONS[3]['price'], "lp": "{:<14}".format(' ')},
            {"left": " ", "right": " ", "name": 'Exit', "price": '', "lp": "{:<15}".format(' ')}
        ]
        self.line = {"left": ">", "right": "<", "name": WEAPONS[1]['name'], "price": WEAPONS[1]['price'], "lp": "  "}
        self.template_line = "|{line[left]}| {line[name]} {line[price]} {line[lp]} |{line[right]}|"
        self.selected_line = WEAPONS[1]['name']
        self.d = None
        self.l = ''

    def find(self):
        for d in self.menu:
            if d["name"] == self.selected_line:
                self.d = d

    def select(self):
        self.find()
        if self.selected_line == "Exit":
            return True
        elif self.selected_line == self.d["name"]:
            if (self.unit.Gold > int(self.d["price"]) or self.unit.Gold == int(self.d["price"])) \
                    and self.d["name"] != self.inv.weapon["name"]:
                self.unit.Gold -= int(self.d["price"])
                self.inv.weapon = self.d
                self.l = self.unit.Gold
            else:
                self.l = 'not enouth Gold or you already have it'

    def render(self):
        self.cls()
        self.selecting()
        print (LIGHT_GRAY("| |your Gold = "+str(self.unit.Gold)+"         | |"))
        for line in self.menu:
            print(LIGHT_GRAY(self.template_line.format(line=line)))
        self.log(self.l)
