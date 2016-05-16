from Classes.main_Unit import *
import random


class Enemy(Main_Unit):
    def __init__(self, fields):
        Main_Unit.__init__(self, fields)
        self.image = 'O'
        self.location = 0
        self.Hit_Points = 10
        self.dmg = 1
        self.find_pos()
        self.update()

    def do_interact(self, dir):
        point_x, point_y = self.directions[dir]()
        if self.field[point_y][point_x] == '⬜':
            self.find_lvl_pos()
            self.tile = '⬜'

    def AI(self):
        dir = random.randint(1, 4)
        if self.Hit_Points != 0 or self.Hit_Points > 0:
            self.field[self.y][self.x] = self.tile
            if self.check_inter(dir):
                self.do_interact(dir)
            elif self.check(dir):
                self.Move(dir)
        else:
            self.field[self.y][self.x] = ""
