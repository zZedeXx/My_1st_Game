from Data.items import *
from Data.colors import *
import copy


class Invent:
    def __init__(self, hero, inventar):
        self.i = 0
        self.hero = hero
        self.weapon = WEAPONS[0]
        self.armor = ARMOR[0]
        self.inventory = copy.deepcopy(inventar)
        self.templ_inv = inventar
        self.over_dmg = hero.dmg + self.weapon['dmg']
        self.draw_inv()

    def draw_inv(self):
        self.inventory[1][0] = self.templ_inv[1][0].format(self.weapon['label'])
        self.inventory[2][0] = self.templ_inv[2][0].format(self.armor['label'])
        self.inventory[3][0] = self.templ_inv[3][0].format(self.over_dmg)
