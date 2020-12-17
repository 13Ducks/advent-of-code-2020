from aocd import get_data
from collections import defaultdict
import itertools

data = get_data(day=17).split("\n")


def init_state():
    state = [
        (i, j, 0, 0)
        for i, r in enumerate(data)
        for j, state in enumerate(r)
        if state == "#"
    ]
    return state


def p1(state):
    neighbors = defaultdict(lambda: 0)
    for x, y, z, w in state:
        for dx, dy, dz in itertools.product([-1, 0, 1], repeat=3):
            if (dx, dy, dz) != (0, 0, 0):
                neighbors[(x + dx, y + dy, z + dz, w)] += 1
    return [
        s for s in neighbors if neighbors[s] == 3 or (s in state and neighbors[s] == 2)
    ]


def p2(state):
    neighbors = defaultdict(lambda: 0)
    for x, y, z, w in state:
        for dx, dy, dz, dw in itertools.product([-1, 0, 1], repeat=4):
            if (dx, dy, dz, dw) != (0, 0, 0, 0):
                neighbors[(x + dx, y + dy, z + dz, w + dw)] += 1
    return [
        s for s in neighbors if neighbors[s] == 3 or (s in state and neighbors[s] == 2)
    ]


state = init_state()
for i in range(6):
    state = p1(state)

print(len(state))

state = init_state()
for i in range(6):
    state = p2(state)

print(len(state))