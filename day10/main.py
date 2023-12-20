# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

MOVES = {
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(1, 0), (0, -1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

def dft(grid, prev_x, prev_y, x, y, visited):
    if prev_x == x and prev_y == y:
        return False
    if grid[y][x] == ".":
        return False
    if grid[y][x] == "S":
        return True
    
    current_pipe = grid[y][x]
    print(f"Current pipe: {current_pipe} at {x}, {y}")

    dx1, dy1 = MOVES[current_pipe][0]
    dx2, dy2 = MOVES[current_pipe][1]

    new_x1, new_y1 = x + dx1, y + dy1
    new_x2, new_y2 = x + dx2, y + dy2

    if new_x1 != x and new_y1 != y:
        new_x, new_y = new_x1, new_y1
    else:
        new_x, new_y = new_x2, new_y2
    

    if new_x < 0 or new_y < 0 or new_x >= len(grid) or new_y >= len(grid[0]):
        return False

    visited.append((new_x, new_y))
    res = dft(grid, x, y, new_x, new_y, visited)
    visited.pop()
    return res


grid = []
for line in open("test.txt"):
    grid.append(list(line.strip()))

start_coords = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == "S"][0]

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

for dx, dy in directions:
    if 0 <= start_coords[0] + dx < len(grid) and 0 <= start_coords[1] + dy < len(grid[0]):
        if grid[start_coords[0] + dx][start_coords[1] + dy] != ".":
            input_coords = (start_coords[0] + dx, start_coords[1] + dy)
            visited = [input_coords]
            print(f"Starting at {input_coords} with {grid[input_coords[0]][input_coords[1]]}")
            if length := dft(grid, start_coords[0], start_coords[1], input_coords[0], input_coords[1], visited):
                print("A MAME HO")
                print(visited)
