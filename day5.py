from aocd import get_data

data = get_data(day=5).split("\n")
data = list(map(lambda x: x.strip(), data))

used = set()
translation = {
    ord("F"): ord("0"),
    ord("L"): ord("0"),
    ord("B"): ord("1"),
    ord("R"): ord("1"),
}

for e in data:
    b = e.translate(translation)
    used.add(int(b, 2))

print(max(used))
print(list(set(range(min(used), max(used))).difference(used))[0])
