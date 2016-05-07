fields = [
    [
        '#######################',
        '#    #         c #  ⬜ #',
        '# H     ✳     c  #    #',
        '#    #       c  f###|##',
        '###### ###########    #',
        '#         f  ✳        #',
        '#          ✳          #',
        '#      ✳              #',
        '#            c        #',
        '#          O          #',
        '#           s         #',
        '#######################'
    ],
    [
        '########',
        '#⬜  ccc#',
        '#   ccc#',
        '#      #',
        '#      #',
        '########'
    ],
    [
        '########',
        '#⬜     #',
        '#      #',
        '########'
    ]
]
for level_num in range(len(fields)):
    fields[level_num] = [list(line) for line in fields[level_num]]


if __name__ == "__main__":
    print(fields[0])
