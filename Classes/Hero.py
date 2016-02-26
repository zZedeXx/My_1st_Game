class Hero:
    def __init__(self, field):
        self.x = None
        self.y = None
        self.image = 'H'
        self.key = False
        self.field = field
        self.find_pos()

    def find_pos(self):
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index(self.image)
                break
            except ValueError:
                j += 1

        if i == -1:
            raise AttributeError("Hero not found")
        else:
            self.x = i
            self.y = j

    def events(self, key):
        self.field[self.y][self.x] = '.'
        if key == 'a':
            if self.look_left():
                self.x -= 1
        elif key == 'd':
            if self.look_right():
                self.x += 1

        if key == 'w':
            if self.look_up():
                self.y -= 1
        elif key == 's':
            if self.look_down():
                self.y += 1

        if self.x >= len(self.field[0]):
            self.x = 0
        elif self.x < 0:
            self.x = len(self.field[0]) - 1

    def look_left(self):
        if self.field[self.y][self.x - 1] == '#' or self.field[self.y][self.x - 1] == '|' and not self.key:
            return False
        elif self.field[self.y][self.x - 1] == 'f':
            self.key = True
            return True
        else:
            return True

    def look_right(self):
        if self.field[self.y][self.x + 1] == '#' or self.field[self.y][self.x + 1] == '|' and not self.key:
            return False
        elif self.field[self.y][self.x + 1] == 'f':
            self.key = True
            return True
        else:
            return True

    def look_up(self):
        if self.field[self.y - 1][self.x] == '#' or self.field[self.y - 1][self.x] == '|' and not self.key:
            return False
        elif self.field[self.y - 1][self.x] == 'f':
            self.key = True
            return True
        else:
            return True

    def look_down(self):
        if self.field[self.y + 1][self.x] == '#' or self.field[self.y + 1][self.x] == '|' and not self.key:
            return False
        elif self.field[self.y+1][self.x] == 'f':
            self.key = True
            return True
        else:
            return True

    def update(self):
        self.field[self.y][self.x] = self.image