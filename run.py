from Classes.Menu import Menu
from Classes.Game import Game
from Data.Levels import fields

menu = Menu()
game = Game()
menu.render()
menu.run()

while True:
    if menu.selected_line != "Exit":
        if menu.start > 0:
            menu.start -= 1
            game.render(game.check(fields), game.status_bar, game.inv.inventory)
            game.run()
            menu.render()
            menu.run()
    else:
        break
