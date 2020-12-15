from aocd import get_data
from collections import defaultdict

data = list(map(int, get_data(day=15).split(",")))
# data = list(map(int, open("temp.txt").read().split(",")))

spoken = defaultdict(lambda: [None, None])

for i, v in enumerate(data):
    spoken[v][0] = i + 1

last = data[-1]

for i in range(len(data), 30000000):
    if spoken[last][1] == None:
        if None in spoken[0]:
            spoken[0][1] = i + 1
        else:
            spoken[0].sort()
            spoken[0][0] = i + 1
            spoken[0].sort()
        last = 0
    else:
        last = spoken[last][1] - spoken[last][0]
        if spoken[last][0] == None:
            spoken[last][0] = i + 1
        elif spoken[last][1] == None:
            spoken[last][1] = i + 1
        else:
            spoken[last][0] = i + 1
            spoken[last].sort()
    if i % 1000000 == 0:
        print(i, last)
    elif i == 30000000 - 1:
        print(last)

    # print(spoken)
