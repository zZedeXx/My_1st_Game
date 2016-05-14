from Data.items import *
from Data.colors import *


class Invent:
    def __init__(self, hero):
        self.i = 0
        self.hero = hero
        self.weapon = WEAPONS[2]
        self.armor = ARMOR[0]
        self.inventory = [
            ['Equipped weapon = {:<11}'],
            ['Equipped  armor = {:<11}'],
            ['Overall  damage = {:<11}'],
        ]
        self.templ_inv = self.inventory
        self.over_dmg = hero.dmg + self.weapon['dmg']
        self.draw_inv()

    def draw_inv(self):
        self.inventory[0][0] = self.templ_inv[0][0].format(self.weapon['label'])
        self.inventory[1][0] = self.templ_inv[1][0].format(self.armor['label'])
        self.inventory[2][0] = self.templ_inv[2][0].format(str(self.over_dmg))
