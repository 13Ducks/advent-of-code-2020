from aocd import get_data

data = get_data(day=6).split("\n\n")
c1 = c2 = 0

for t in data:
    c1 += len(set(t.replace("\n", "")))

    s = set("qwertyuiopasdfghjklzxcvbnm")
    for i in t.split("\n"):
        s &= set(i)
    c2 += len(s)

print(c1, c2)