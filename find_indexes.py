field = [
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '|', '.', '.', 'K', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
    ['#', '.', '.', 'H', '.', '.', '.', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ']
]

# res = field[1].index("H")

j = 0
i = -1
for line in field:
    try:
        i = line.index("H")
        break
    except ValueError:
        j += 1
        pass
if i == -1:
    print("Hero not found")
else:
    print(i, j)