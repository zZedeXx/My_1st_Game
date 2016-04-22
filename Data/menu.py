import run


class Menu:
    def __init__(self):
        self.menu = [
             {"left": " ", "right": " ", "name": "Start"},
             {"left": " ", "right": " ", "name": "Options"},
             {"left": " ", "right": " ", "name": "Exit"},
        ]
        self.line = {"left": ">", "right": "<", "name": "Start"}
        self.template_line = "|{line[left]}| {line[name]} |{line[right]}|"
        self.selected_line = "Start"
        self.i = 0

    def events(self, key):
        if key == "w":
            self.i -= 1
            try:
                self.selected_line = self.menu[self.i]['name']
            except IndexError:
                self.selected_line = self.selected_line
                self.i += 1
            self.selecting()
            return False
        elif key == "s":
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
            return True
        elif self.selected_line == "Options":
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
        self.selecting()
        for line in self.menu:
            print(self.template_line.format(line=line))
