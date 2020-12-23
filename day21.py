from aocd import get_data
from collections import defaultdict

data = get_data(day=21).split("\n")
# data = open("temp.txt").read().split("\n")
pot = defaultdict(lambda: [])
all_ing = []

for i in data:
    ing, al = i.replace("(", "").replace(")", "").split(" contains ")
    ing = set(ing.split(" "))
    all_ing.append(ing)
    al = al.split(", ")
    for a in al:
        pot[a].append(ing)

for k, v in pot.items():
    pot[k] = v[0].intersection(*v[1:])

while True:
    for k1, v1 in pot.items():
        if len(v1) == 1:
            for k2, v2 in pot.items():
                if k1 != k2:
                    v2.discard(min(v1))
                    pot[k2] = v2

    finished = True
    for v1 in pot.values():
        if len(v1) != 1:
            finished = False
            break

    if finished:
        break

al = list(pot.values())
al = al[0].union(*al[1:])

p1 = sum([len(i - al) for i in all_ing])
print(p1)

danger = sorted(list(pot.items()))
p2 = ",".join([min(i[1]) for i in danger])
print(p2)