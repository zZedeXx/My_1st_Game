from Data.items import *


class Invent:
    def __init__(self, hero):
        self.hero = hero
        self.weapon = WEAPONS[0]
        self.armor = ARMOR[0]
        self.inventory = [
            ['Equipped weapon = {:<11}'.format(self.weapon['label'])],
            ['Equipped  armor = {:<11}'.format(self.armor['label'])],
            ['Overall  damage = {:<11}'.format(self.weapon['dmg'])],
            #['Keys = {:<22}'.format(self.hero.key)],
            #['Gold = {:<22}'.format(self.hero.Gold)]
        ]
