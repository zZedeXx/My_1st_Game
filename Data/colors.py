RED = lambda s: "\033[1;31m{}\033[1;39m".format(s)
GREEN = lambda s: "\033[1;32m{}\033[1;39m".format(s)
YELLOW_FOREGROUND = lambda s: "\033[1;33m{}\033[1;39m".format(s)
BLUE = lambda s: "\033[1;34m{}\033[1;39m".format(s)
BLACK = lambda s: "\033[1;30m{}\033[1;39m".format(s)
WHITE = lambda s: "\033[1;97m{}\033[1;39m".format(s)
DARK_GRAY = lambda s: "\033[1;90m{}\033[1;39m".format(s)
LIGHT_GRAY = lambda s: "\033[1;37m{}\033[1;39m".format(s)
LIGHT_GREEN = lambda s: "\033[1;92m{}\033[1;39m".format(s)
LIGHT_YELLOW = lambda s: "\033[1;93m{}\033[1;39m".format(s)
LIGHT_MAGENTA = lambda s: "\033[1;95m{}\033[1;39m".format(s)
LIGHT_CYAN = lambda s: "\033[1;96m{}\033[1;39m".format(s)
BG_WHITE = lambda s: "\033[1;107m{}\033[1;49m".format(s)
BG_BLACK = lambda s: "\033[1;40m{}\033[1;49m".format(s)
BG_BLUE = lambda s: "\033[1;44m{}\033[1;49m".format(s)
BG_LIGHT_BLUE = lambda s: "\033[1;104m{}\033[1;49m".format(s)
BG_LIGHT_YELLOW = lambda s: "\033[1;103m{}\033[1;49m".format(s)
BG_RED = lambda s: "\033[1;41m{}\033[1;49m".format(s)