from aocd import get_data

data = get_data(day=3).split("\n")
data = list(map(lambda x: x.strip(), data))


def solve(x, y):
    curr = [0, 0]
    cnt = 0
    while curr[1] < len(data):
        c = data[curr[1]][curr[0]]
        if c == "#":
            cnt += 1

        curr[0] += x
        curr[1] += y

        curr[0] %= len(data[0])
    return cnt


print(solve(3, 1))
print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
