class Main_Unit:
    def __init__(self, fields):
        self.x = None
        self.y = None
        self.f = fields
        self.tile = None
        self.field = fields[0]

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
            raise AttributeError("Unit not found")
        else:
            self.x = i
            self.y = j

    def find_lvl_pos(self):
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index('⬜')
                break
            except ValueError:
                j += 1

        if i == -1:
            raise AttributeError("Hero not found")
        else:
            self.x = i
            self.y = j

    def look_left(self):
        """
        Check wall or door left
        """
        if self.field[self.y][self.x - 1] == '#' or self.field[self.y][self.x - 1] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_right(self):
        """
        Check wall or door right
        """
        if self.field[self.y][self.x + 1] == '#' or self.field[self.y][self.x + 1] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_up(self):
        """
        Check wall or door up
        """
        if self.field[self.y - 1][self.x] == '#' or self.field[self.y - 1][self.x] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_down(self):
        """
        Check wall or door down
        """
        if self.field[self.y + 1][self.x] == '#' or self.field[self.y + 1][self.x] == '|' and self.key == 0:
            return False
        else:
            return True

    def update(self):
        self.field[self.y][self.x] = self.image
