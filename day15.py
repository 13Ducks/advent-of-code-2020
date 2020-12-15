from aocd import get_data

data = list(map(int, get_data(day=15).split(",")))

last = {v: i + 1 for i, v in enumerate(data)}
prev = data[-1]

for i in range(len(data), 30000000):
    if prev in last:
        nxt = i - last[prev]
        last[prev] = i
        prev = nxt
    else:
        last[prev] = i
        prev = 0

    if i + 1 == 2020:
        print(prev)

print(prev)
