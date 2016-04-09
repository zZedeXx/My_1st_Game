from Classes.Main_Unit import *


class Enemy(Main_Unit):
    def __init__(self, fields):
        Main_Unit.__init__(self, fields)
        self.image = 'O'
        self.Hit_Points = 100

    def AI(self):
        self.x += 1

