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

GAME_OBJECTS = [
    {"label": "Hero", "char": "H", "icon": 'ⵅ', "passable": True, "interactive": False, "do": None},
    {"label": "Wall", "char": "#", "icon": '▓', "passable": False, "interactive": False, "do": None},
    {"label": "Door", "char": "|", "icon": '☗', "passable": False, "interactive": True, "do": open_door},
    {"label": "Key", "char": "f", "icon": "⚷", "passable": True, "interactive": True, "do": get_key},
    {"label": "coin", "char": "c", "icon": "➄", "passable": True, "interactive": True, "do": add_gold},
    {"label": "Exit", "char": "⬜", "icon": "⨅", "passable": True, "interactive": True, "do": change_lvl},
    {"label": "Trap", "char": "✳", "icon": ' ', "passable": True, "interactive": True, "do": hit}
]

IMPASSIBLE_OBJECTS = [obj["char"]for obj in GAME_OBJECTS if not obj["passable"]]
INTERACTIVE_OBJECTS = [obj["char"] for obj in GAME_OBJECTS if obj["interactive"]]