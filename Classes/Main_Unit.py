LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
from Data import Objects
from Data.Levels import fields


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
