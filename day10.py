from aocd import get_data
from functools import lru_cache

data = sorted([0, *map(int, get_data(day=10).split("\n"))])

cnts = [0, 0]
for i in range(1, len(data)):
    d = data[i] - data[i - 1]
    if d == 1:
        cnts[0] += 1
    if d == 3:
        cnts[1] += 1
print(cnts[0] * (cnts[1] + 1))

poss = {}
for i in range(len(data)):
    adj = []
    for j in range(i + 1, len(data)):
        d = data[j] - data[i]
        if d <= 3:
            adj.append(j)
        else:
            break
    poss[i] = adj


@lru_cache(maxsize=None)
def count_ways(v):
    if not poss[v]:
        return 1
    return sum(count_ways(x) for x in poss[v])


print(count_ways(0))