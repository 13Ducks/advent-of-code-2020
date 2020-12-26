from aocd import get_data
from aocd import get_data
from collections import defaultdict

data = get_data(day=24).splitlines()

directions = {
    "se": (1, -1),
    "e": (1, 0),
    "ne": (0, 1),
    "nw": (-1, 1),
    "w": (-1, 0),
    "sw": (0, -1),
}

state = []

for i in data:
    curr = 0
    x = y = 0
    while curr < len(i):
        next_dir = None
        if i[curr : curr + 1] in directions.keys():
            next_dir = i[curr : curr + 1]
            curr += 1
        else:
            next_dir = i[curr : curr + 2]
            curr += 2
        x += directions[next_dir][0]
        y += directions[next_dir][1]

    if (x, y) in state:
        state.remove((x, y))
    else:
        state.append((x, y))

print(len(state))


def turn():
    neighbors = defaultdict(lambda: 0)
    for x, y in state:
        for dx, dy in directions.values():
            neighbors[(x + dx, y + dy)] += 1

    return [
        s for s in neighbors if neighbors[s] == 2 or (s in state and neighbors[s] == 1)
    ]


for _ in range(100):
    state = turn()

print(len(state))