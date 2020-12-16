from aocd import get_data
import re

data = list(map(lambda x: x.split("\n"), get_data(day=16).split("\n\n")))

rules = []
near = []
my = [*map(int, data[1][1].split(","))]
check = lambda v, r: r[0] <= v <= r[1] or r[2] <= v <= r[3]
p1, p2 = 0, 1

for rule in data[0]:
    spl = re.split(r": | or |-", rule)
    rules.append([*map(int, spl[1:])])

for ticket in data[2][1:]:
    valid = True
    ticket = [*map(int, ticket.split(","))]
    for v in ticket:
        good = any([check(v, r) for r in rules])
        if not good:
            p1 += v
            valid = False
    if valid:
        near.append(ticket)

print(p1)

potential = {i: set() for i in range(len(rules))}

for i, r in enumerate(rules):
    for j in range(len(rules)):
        works = all(check(t[j], r) for t in near)
        if works:
            potential[i].add(j)

final = [-1] * len(rules)
potential = sorted(potential.items(), key=lambda x: len(x[1]))
seen = set()

for i in potential:
    v = (i[1] - seen).pop()
    seen.add(v)
    final[i[0]] = v

for i in range(6):
    p2 *= my[final[i]]

print(p2)