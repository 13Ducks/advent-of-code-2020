from aocd import get_data
from collections import defaultdict

data = get_data(day=17).split("\n")
nx, ny = len(data[0]), len(data)


def initial_grid(data):
    grid = defaultdict(lambda: 0)
    for i, r in enumerate(data):
        for j in range(len(r)):
            if r[j] == "#":
                grid[(j, i, 0, 0)] = 1
    return grid


def count_neighbors(x, y, z, w, grid):
    active = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if (dx, dy, dz, dw) != (0, 0, 0, 0) and grid[
                        (x + dx, y + dy, z + dz, w + dw)
                    ] == 1:
                        active += 1
    return active


def cycle(grid, n, p1):
    if p1:
        min_w, max_w = 0, 1
    else:
        min_w, max_w = -n - 1, n + 2
    new_grid = defaultdict(lambda: 0)
    for x in range(-n - 1, nx + n + 1):
        for y in range(-n - 1, ny + n + 1):
            for z in range(-n - 1, n + 2):
                for w in range(min_w, max_w):
                    p = (x, y, z, w)
                    num_neighbors = count_neighbors(*p, grid)
                    if grid[p] == 0 and num_neighbors == 3:
                        new_grid[p] = 1
                    if grid[p] == 1 and (num_neighbors in (2, 3)):
                        new_grid[p] = 1
    return new_grid


grid = initial_grid(data)
for i in range(6):
    grid = cycle(grid, i, True)

print(list(grid.values()).count(1))

grid = initial_grid(data)
for i in range(6):
    grid = cycle(grid, i, False)

print(list(grid.values()).count(1))