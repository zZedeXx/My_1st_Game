from Data.Objects import *
from Data.Levels import fields
from Classes.battle import Battle
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

class Main_Unit:
    def __init__(self, fields):
        self.x = None
        self.y = None
        self.tile = ' '
        self.field = fields[0]
        self.directions = {LEFT: self.get_pos((-1, 0)),
                           RIGHT: self.get_pos((1, 0)),
                           UP: self.get_pos((0, -1)),
                           DOWN: self.get_pos((0, 1))}

    def find_pos(self):
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index(self.image)
                break
            except ValueError:
                j += 1
        if i == -1:
            raise AttributeError("Unit not found")
        else:
            self.x = i
            self.y = j

    def find_lvl_pos(self):
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index('⬜')
                break
            except ValueError:
                j += 1
        if i == -1:
            raise AttributeError("Hero not found")
        else:
            self.x = i
            self.y = j

    def get_field(self):
        if self.location == 0:
            self.field = fields[1]
            self.location += 1
            self.find_lvl_pos()
        elif self.location == 1:
            self.field = fields[0]
            self.location -= 1
            self.find_lvl_pos()

    def check_inter(self, dir):
        point_x, point_y = self.directions[dir]()
        if self.field[point_y][point_x] in INTERACTIVE_OBJECTS:
            return True
        else:
            return False

    def do_interact(self, dir):
        point_x, point_y = self.directions[dir]()
        for obj in GAME_OBJECTS:
            try:
                if obj.get("char") == self.field[point_y][point_x] :
                    for en_obj in ENEMY_UNITS:
                        if en_obj.get("char") != self.field[point_y][point_x]:
                            obj["do"](self, point_x, point_y)
                        else:
                            Battle(self, en_obj.get("class"))
            except IndexError:
                self.find_lvl_pos()
                self.tile = '⬜'

    def check(self, dir):
        point_x, point_y = self.directions[dir]()
        if self.field[point_y][point_x] in IMPASSIBLE_OBJECTS:
            return False
        else:
            return True

    def Move(self, dir):
        point_x, point_y = self.directions[dir]()
        self.field[self.y][self.x] = self.tile
        self.tile = self.field[point_y][point_x]
        self.field[point_y][point_x] = self.image
        self.x, self.y = point_x, point_y

    def get_pos(self, dir):
        def W():
            return self.x + dir[0], self.y + dir[1]
        return W

    def update(self):
        self.field[self.y][self.x] = self.image
