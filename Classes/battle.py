from Classes.Menu import *


class Battle(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.menu = [
            {"left": " ", "right": " ", "name": "Attack", "lp": "{:<2}".format(' ')},
            {"left": " ", "right": " ", "name": "Spells", "lp": "{:<2}".format(' ')},
            {"left": " ", "right": " ", "name": "Items", "lp": "{:<3}".format(' ')},
            {"left": " ", "right": " ", "name": "Run", "lp": "{:<5}".format(' ')}
        ]
        self.line = {"left": ">", "right": "<", "name": "Attack", "lp": "  "}
        self.selected_line = self.menu[0]["name"]

    def select(self):
        if self.selected_line == "Attack":
            pass
        elif self.selected_line == "Run":
            return True

    def render(self):
        i = 0
        lin = ''
        self.cls()
        self.selecting()
        for line in self.menu:
            if i == 2:
                i = 0
                print(lin)
                lin = ''
            lin += self.template_line.format(line=line)
            i += 1
        print(lin)