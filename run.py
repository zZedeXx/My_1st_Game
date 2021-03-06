from Classes.menu import Menu
from Classes.game import Game
from Data.Levels import fields

menu = Menu()
game = Game()
menu.render()
menu.run()

while True:
    if menu.selected_line != "Exit":
        if menu.start > 0:
            menu.start -= 1
            game.render(' ', game.check(fields), game.status_bar, game.invent)
            game.run()
            menu.render()
            menu.run()
    else:
        break
