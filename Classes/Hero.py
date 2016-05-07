import copy
from Classes.Main_Unit import *
from Data.inventory import Invent

class Hero(Main_Unit):
    def __init__(self, fields, status_bar):
        Main_Unit.__init__(self, fields)
        self.inv = Invent(self)
        self.key_up = 'w'
        self.key_down = 's'
        self.key_left = 'a'
        self.key_right = 'd'
        self.image = 'H'
        self.Hit_Points = 100
        self.Mana_Points = 100
        self.Gold = 0
        self.EXP = 0
        self.level = 0
        self.key = 0
        self.field = fields[0]
        self.find_pos()
        self.location = 0
        self.status_bar = copy.deepcopy(status_bar)
        self.template_status_bar = status_bar
        self.update()

    def draw_status(self):
        self.status_bar[1][0] = self.template_status_bar[1][0].format(self.Hit_Points)
        self.status_bar[2][0] = self.template_status_bar[2][0].format(self.Mana_Points)
        self.status_bar[3][0] = self.template_status_bar[3][0].format(self.EXP)
        self.status_bar[4][0] = self.template_status_bar[4][0].format(self.level)

    def events(self, key):
        self.field[self.y][self.x] = self.tile
        if key == self.key_left or key == "D":
            dir = LEFT
        elif key == self.key_right or key == "C":
            dir = RIGHT
        elif key == self.key_up or key == "A":
            dir = UP
        elif key == self.key_down or key == "B":
            dir = DOWN
        elif key == 'i':
            return False
        else:
            self.field[self.y][self.x] = self.image
            return

        if self.check_inter(dir):
            self.do_interact(dir)
        elif self.check(dir):
            self.Move(dir)

    def update(self):
        self.field[self.y][self.x] = self.image
        self.draw_status()
