from aocd import get_data

data = list(map(int, get_data(day=9).split("\n")))


def find_add(data, target):
    s = set([target - i for i in data])
    for i in data:
        if i in s and 2 * i != target:
            return True
    return False


def find_set(data, target):
    s = data[0]
    start = 0
    for i in range(1, len(data)):
        while s > target:
            s -= data[start]
            start += 1

        if s == target and start != i - 1:
            r = data[start : i - 1]
            return max(r) + min(r)

        s += [i]


pre_len = 25
bad = None

for i, v in enumerate(data[pre_len:]):
    a = find_add(data[i : i + pre_len], v)
    if not a:
        bad = v
        break

print(bad)
print(find_set(data, bad))
