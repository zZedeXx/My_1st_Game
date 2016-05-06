from Data.items import *


class Invent:
    def __init__(self):
        self.weapon = WEAPONS[0]
        self.armor = 'shirt'
        self.inventory = [
            ['Equiped weapon = {:<11}'.format(self.weapon['label'])],
            ['Equiped  armor = {:<11}'.format(self.armor)],
            ['Overall   dmg  = {:<11}'.format()]
        ]
