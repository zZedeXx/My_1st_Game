from Classes.Main_Unit import *
import random


class Enemy(Main_Unit):
    def __init__(self, fields):
        Main_Unit.__init__(self, fields)
        self.image = 'O'
        self.location = 0
        self.Hit_Points = 10
        self.alive = True
        self.find_pos()
        self.update()

    def AI(self):
        if self.alive:
            self.field[self.y][self.x] = self.tile
            #self.Move(LEFT)
        else:
            self.field[self.y][self.x] = ' '
