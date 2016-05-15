from Data.colors import *
from Data.items import *
from Classes.battle import *


def hit(hero, ob_x, ob_y):
    hero.Hit_Points -= 10
    hero.update()


def get_key(hero, ob_x, ob_y):
    hero.key += 1
    hero.field[ob_y][ob_x] = ' '


def change_lvl(hero, ob_x, ob_y):
    hero.get_field()
    hero.tile = '⬜'


def open_door(hero, ob_x, ob_y):
    if hero.key == 0:
        None
    else:
        hero.key -= 1
        hero.field[ob_y][ob_x] = ' '


def add_gold(hero, ob_x, ob_y):
    hero.Gold += 5
    hero.field[ob_y][ob_x] = ' '


def buy(hero, ob_x, ob_y):

    hero.sh.render()
    hero.sh.run()


def beat(hero, ob_x, ob_y):
    Battle(hero, ).render()
    hero.beat.run()

GAME_OBJECTS = [
    {"label": "Enemy", "char": "O", "icon": RED('O'), "passable": False, "interactive": True, "do": beat},
    {"label": "Hero", "char": "H", "icon": LIGHT_CYAN('Ω'), "passable": True, "interactive": False, "do": None},
    {"label": "Wall", "char": "#", "icon": DARK_GRAY('▓'), "passable": False, "interactive": False, "do": None},
    {"label": "Door", "char": "|", "icon": YELLOW_FOREGROUND('☗'), "passable": False, "interactive": True, "do": open_door},
    {"label": "Key", "char": "f", "icon": LIGHT_YELLOW("⚷"), "passable": True, "interactive": True, "do": get_key},
    {"label": "coin", "char": "c", "icon": LIGHT_YELLOW("➄"), "passable": True, "interactive": True, "do": add_gold},
    {"label": "Exit", "char": "⬜", "icon": LIGHT_GRAY("∩"), "passable": True, "interactive": True, "do": change_lvl},
    {"label": "Trap", "char": "✳", "icon": WHITE("✳"), "passable": True, "interactive": True, "do": hit},
    {"label": "Shop", "char": "s", "icon": GREEN("M"), "passable": False, "interactive": True, "do": buy}
]

IMPASSIBLE_OBJECTS = [obj["char"]for obj in GAME_OBJECTS if not obj["passable"]]
INTERACTIVE_OBJECTS = [obj["char"] for obj in GAME_OBJECTS if obj["interactive"]]
ICONS = {obj['char']: obj["icon"] for obj in GAME_OBJECTS}