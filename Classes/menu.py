import tty, termios, sys, os
from Data.colors import *


class Menu:
    def __init__(self):
        self.menu = [
            {"left": " ", "right": " ", "name": "Start", "lp": "{:<12}".format(' ')},
            {"left": " ", "right": " ", "name": "Options", "lp": "{:<10}".format(' ')},
            {"left": " ", "right": " ", "name": "Exit", "lp": "{:<13}".format(' ')},
        ]
        self.line = {"left": ">", "right": "<", "name": "Start", "lp": "  "}
        self.template_line = "|{line[left]}| {line[name]}{line[lp]} |{line[right]}|"
        self.selected_line = "Start"
        self.i = 0
        self.start = 0

    def options(self):
        #print('conf input')
        #self.unit.key_left = input('key left :')
        #self.unit.key_right = input('key right :')
        #self.unit.key_up = input('key up :')
        #self.unit.key_down = input('key down :')
        pass

    def log(self, l):
        print (LIGHT_GRAY(l))

    def events(self, key):
        if key == "w" or key == "A":
            self.i -= 1
            try:
                self.selected_line = self.menu[self.i]['name']
            except IndexError:
                self.selected_line = self.selected_line
                self.i += 1
            self.selecting()
            return False
        elif key == "s" or key == "B":
            self.i += 1
            try:
                self.selected_line = self.menu[self.i]['name']
            except IndexError:
                self.selected_line = self.selected_line
                self.i -= 1
            self.selecting()
            return False
        elif key == "\r":
            return self.select()

    def select(self):
        if self.selected_line == "Start":
            print('Game Starting')
            self.start += 1
            return True
        elif self.selected_line == "Options":
            self.options()
            return False
        elif self.selected_line == "Exit":
            return True

    def selecting(self):
        for line in self.menu:
            if line["name"] == self.selected_line:
                line["left"] = ">"
                line["right"] = "<"
            else:
                line["left"] = " "
                line["right"] = " "

    def render(self):
        self.cls()
        self.selecting()
        for line in self.menu:
            print(LIGHT_GRAY(self.template_line.format(line=line)))

    def getchar(self):
        """
        Returns a single character from standard input
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def cls(self):
        """
        Очищаем консоль
        """
        os.system(['clear', 'cls'][os.name == 'nt'])

    def run(self):
        while True:
            c = self.getchar()
            if self.events(c):
                break
            self.cls()
            self.render()
