# inter_obj = {'✳':
#
# }
import copy


class Logs:
    def __init__(self):
        self.logs = []

    def add_message(self, message):
        if message not in self.logs:
            self.logs.append(message)

    def render(self):
        for line in self.logs:
            print(line)


class Hero:
    def __init__(self, field, field2, status_bar, logs):
        self.x = None
        self.y = None
        self.image = 'H'
        self.Hit_Points = 100
        self.Mana_Points = 100
        self.Gold = 0
        self.EXP = 0
        self.level = 0
        self.key = 0
        self.f = field2
        self.field = field
        self.status_bar = copy.deepcopy(status_bar)
        self.template_status_bar = status_bar
        self.find_pos()
        self.logs = logs
        self.update()

    def draw_status(self):
        # self.Hit_Points += 10
        # self.logs.add_message(self.Hit_Points)
        self.status_bar[1][0] = self.template_status_bar[1][0].format(self.Hit_Points)
        self.status_bar[2][0] = self.template_status_bar[2][0].format(self.Mana_Points)
        self.status_bar[3][0] = self.template_status_bar[3][0].format(self.Gold)
        self.status_bar[4][0] = self.template_status_bar[4][0].format(self.EXP)
        self.status_bar[5][0] = self.template_status_bar[5][0].format(self.level)
        self.status_bar[6][0] = self.template_status_bar[6][0].format(self.key)

    def collide_objects(self):
        if self.field[self.y][self.x] == "✳":
            self.Hit_Points -= 10
        elif self.field[self.y][self.x] == 'f':
            self.key += 1
        elif self.field[self.y][self.x] == '|':
            self.key -= 1
        elif self.field[self.y][self.x] == '⬜':
            self.field = self.f

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
        elif key == 'w':
            if self.look_up():
                self.y -= 1
        elif key == 's':
            if self.look_down():
                self.y += 1



    def look_left(self):
        if self.field[self.y][self.x - 1] == '#' or self.field[self.y][self.x - 1] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_right(self):
        """
        Check wall right
        """
        if self.field[self.y][self.x + 1] == '#' or self.field[self.y][self.x + 1] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_up(self):
        if self.field[self.y - 1][self.x] == '#' or self.field[self.y - 1][self.x] == '|' and self.key == 0:
            return False
        else:
            return True

    def look_down(self):
        if self.field[self.y + 1][self.x] == '#' or self.field[self.y + 1][self.x] == '|' and self.key == 0:
            return False
        else:
            return True

    def update(self):
        self.collide_objects()
        self.field[self.y][self.x] = self.image
        self.draw_status()
