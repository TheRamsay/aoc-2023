from typing import List, DefaultDict
from collections import defaultdict, OrderedDict

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
]

def parse():
    return open("./input.txt").readlines();


def part1():
    valid = []
    data = parse()

    buffer = ""
    good = False

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if not val.isnumeric():
                # End of the number
                if buffer != "" and good:
                    valid.append(int(buffer))

                good = False
                buffer = ""
                continue

            if val.isnumeric():
                buffer += val

                # Number is already valid
                if good:
                    continue


                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if x >= 0 and x < len(data) and y >= 0 and y < len(row):
                        if not data[x][y].isnumeric() and data[x][y] != "." and data[x][y] != "\n":
                            good = True
                            break

    if good:
        valid.append(int(buffer))

    print(sum(valid))

def part2():
    acc = 0

    valid = []

    gears = defaultdict(list)

    data = parse()

    buffer = ""
    good = False

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if not val.isnumeric():
                if buffer != "" and good:
                    valid.append(int(buffer))
                    gears[(gear_x, gear_y)].append(int(buffer))

                good = False
                buffer = ""
                continue

            if val.isnumeric():
                buffer += val
                if good:
                    continue

                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if x >= 0 and x < len(data) and y >= 0 and y < len(row):
                        if data[x][y] == "*":
                            good = True
                            gear_x, gear_y = x, y
                            break

    if good:
        valid.append(int(buffer))
        gears[(gear_x, gear_y)].append(int(buffer))

    
    for k, v in gears.items():
        if len(v) == 2:
            acc += v[0] * v[1]

    print(acc)

part1()
part2()
