from time import sleep
from queue import deque
import re

def part1():
    acc = 0

    for line in open("./input.txt", "r").readlines():
        winning, mine = line.strip().split("|")
        winning = winning.split(":")[1]
        winning = {int(x) for x in winning.strip().split(" ") if x != ""}
        mine = {int(x) for x in mine.strip().split(" ") if x != ""}

        same = winning.intersection(mine)

        if len(same) > 0:
            x = 2 ** (len(same) - 1)
            acc += x    


    return acc


def part2():
    data = open("./input.txt", "r").readlines()
    counts = [1] * len(data)

    for i, line in enumerate(data):
        winning, mine = line.strip().split("|")
        winning = winning.split(":")[1]
        winning = {int(x) for x in winning.strip().split(" ") if x != ""}
        mine = {int(x) for x in mine.strip().split(" ") if x != ""}

        same = winning.intersection(mine)

        for j in range(len(same)):
            counts[i + 1 + j] += counts[i]
            
    return sum(counts)  

print(part1())
print(part2())
