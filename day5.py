from aocd import get_data

data = get_data(day=5).split("\n")
data = list(map(lambda x: x.strip(), data))


def bin_search(lower, upper, pattern):
    if len(pattern) == 0:
        return lower

    mid = (lower + (upper - 1)) // 2
    if pattern[0] in ["F", "L"]:
        return bin_search(lower, mid, pattern[1:])
    else:
        return bin_search(mid + 1, upper, pattern[1:])


used = set()
for e in data:
    r = bin_search(0, 127, e[:7])
    c = bin_search(0, 7, e[7:])
    used.add(r * 8 + c)

print(max(used))
print(list(set(range(min(used), max(used))).difference(used))[0])
