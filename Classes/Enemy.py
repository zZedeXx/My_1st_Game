from Classes.Main_Unit import *
from Data.colors import *
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

    def AI(self, dir=LEFT):
        if self.Hit_Points != 0 or self.Hit_Points > 0:
            self.field[self.y][self.x] = self.tile
            if self.check_inter(dir):
                self.do_interact(dir)
            elif self.check(dir):
                self.Move(dir)
        else:
            self.field.pop([self.y][self.x])
