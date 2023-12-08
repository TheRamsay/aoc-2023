from time import sleep
import math

data = open("test.txt", "r").readlines()

pattern = data[0].strip()
cursor = 0

map_ = {}

for line in data[1:]:
    if line == "\n":
        continue

    src, dest = line.strip().split(" = ")
    dest = dest.replace(")", "").replace("(", "")
    dest_l, dest_r = dest.split(", ")

    map_[src] = (dest_l, dest_r)

starts = [k for k in map_.keys() if "A" in k]
steps_arr = []

for start in starts:
    current = start
    steps = 0

    while "Z" not in current:
        dest_l, dest_r = map_[current]

        if pattern[steps % len(pattern)] == "L":
            current = dest_l
        else:
            current = dest_r

        steps += 1

    steps_arr.append(steps)

print(math.lcm(*steps_arr))