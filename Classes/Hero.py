import copy
from Data import Objects
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
        self.status_bar[1][0] = self.template_status_bar[1][0].format(self.Hit_Points)
        self.status_bar[2][0] = self.template_status_bar[2][0].format(self.Mana_Points)
        self.status_bar[3][0] = self.template_status_bar[3][0].format(self.Gold)
        self.status_bar[4][0] = self.template_status_bar[4][0].format(self.EXP)
        self.status_bar[5][0] = self.template_status_bar[5][0].format(self.level)
        self.status_bar[6][0] = self.template_status_bar[6][0].format(self.key)

    def events(self, key):
        self.field[self.y][self.x] = self.tile
        if key == 'a':
            dir = LEFT
        elif key == 'd':
            dir = RIGHT
        elif key == 'w':
            dir = UP
        elif key == 's':
            dir = DOWN
        else:
            self.field[self.y][self.x] = self.image
            return

        if self.check_inter(dir):
            self.do_interact(dir)
        elif self.check(dir):
            self.Move(dir)

    def check_inter(self, dir):
        point_x, point_y = self.directions[dir]()
        if self.field[point_y][point_x] in Objects.INTERACTIVE_OBJECTS:
            return True
        else:
            return False

    def do_interact(self, dir):
        point_x, point_y = self.directions[dir]()
        for obj in Objects.GAME_OBJECTS:
            if obj.get("char") == self.field[point_y][point_x]:
                obj["do"](self, point_x, point_y)

    def check(self, dir):
        point_x, point_y = self.directions[dir]()
        if self.field[point_y][point_x] in Objects.IMPASSIBLE_OBJECTS:
            return False
        else:
            return True

    def update(self):
        self.field[self.y][self.x] = self.image
        self.draw_status()
