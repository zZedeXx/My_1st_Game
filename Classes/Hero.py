# inter_obj = {'✳':
#
# }
import copy
from Classes.Main_Unit import *

class Hero(Main_Unit):
    def __init__(self, fields, status_bar):
        Main_Unit.__init__(self, fields)
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
        # self.Hit_Points += 10
        # self.logs.add_message(self.Hit_Points)
        self.status_bar[1][0] = self.template_status_bar[1][0].format(self.Hit_Points)
        self.status_bar[2][0] = self.template_status_bar[2][0].format(self.Mana_Points)
        self.status_bar[3][0] = self.template_status_bar[3][0].format(self.Gold)
        self.status_bar[4][0] = self.template_status_bar[4][0].format(self.EXP)
        self.status_bar[5][0] = self.template_status_bar[5][0].format(self.level)
        self.status_bar[6][0] = self.template_status_bar[6][0].format(self.key)

    def collide_objects(self):
        if self.field[self.y][self.x] == "✳":
            self.Hit_Points -= 10
        elif self.field[self.y][self.x] == self.image:
            self.tile = ' '
        elif self.field[self.y][self.x] == 'f':
            self.key += 1
            self.tile = ' '
        elif self.field[self.y][self.x] == '|':
            self.key -= 1
            self.tile = ' '
        elif self.field[self.y][self.x] == '⬜':
            self.get_field()
            self.tile = self.field[self.y][self.x]
        else:
            self.tile = self.field[self.y][self.x]

    def events(self, key):
        self.field[self.y][self.x] = self.tile
        if key == 'a':
            if self.look_left():
                self.x -= 1
        elif key == 'd':
            if self.look_right():
                self.x += 1
        elif key == 'w':
            if self.look_up():
                self.y -= 1
        elif key == 's':
            if self.look_down():
                self.y += 1

    def get_field(self):
        if self.location == 0:
            self.field = self.f[1]
            self.location += 1
            self.find_lvl_pos()
        elif self.location == 1:
            self.field = self.f[0]
            self.location -= 1
            self.find_lvl_pos()

    def update(self):
        self.collide_objects()
        self.field[self.y][self.x] = self.image
        self.draw_status()
