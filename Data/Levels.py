fields = [
    [
        '##############',
        '⬜      ###   #',
        '#       |    #',
        '#    #####   #',
        '#  ✳ #f# #####',
        '#    # # # H #',
        '### ## ###   #',
        '#      # #   #',
        '#  ✳  ✳      #',
        '#      # #   #',
        '#      # #####',
        '##########    '
    ],
    [
        '########',
        '#  ✳✳✳ #',
        '#    ✳ #',
        '#    ✳ #',
        '#    ✳ ',
        '########'
    ]
]
for level_num in range(len(fields)):
    fields[level_num] = [list(line) for line in fields[level_num]]
print(fields[0])
