
verticies = []

current_x = 0
current_y = 0

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

for line in open("test.txt").readlines():
    direction, distance, color = line.split()
    distance = int(distance)

    dx, dy = directions[direction]

    current_x += dx * distance
    current_y += dy * distance

    verticies.append((current_x, current_y))


print(verticies)
print(len(verticies))


from shapely.geometry import Polygon
pgon = Polygon(verticies) 
print(pgon.area)

