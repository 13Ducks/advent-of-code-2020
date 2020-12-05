from aocd import get_data

data = get_data(day=5).split("\n")
data = list(map(lambda x: x.strip(), data))

used = set()

t = str.maketrans("FBLR", "0101")
for e in data:
    b = e.translate(t)
    used.add(int(b, 2))

print(max(used))
print(*(set(range(min(used), max(used))) - used))

# one liner for fun
# (lambda d: print(max(d), *set(range(min(d), max(d))) - d))(set([int(e.translate(str.maketrans("FBLR", "0101")), 2) for e in get_data(day=5).split("\n")]))
