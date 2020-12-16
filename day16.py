from aocd import get_data
import re

data = get_data(day=16).split("\n\n")
# data = open("temp.txt").read().split("\n\n")

rules = []
tot = 0
check = lambda v, r: r[0] <= v <= r[1] or r[2] <= v <= r[3]
near = []
my = None

for v in data:
    s = v.split("\n")
    if "ticket" in s[0]:
        if "your ticket" in s[0]:
            my = s[1]
        for j in s[1:]:
            valid = True
            for k in j.split(","):
                k = int(k)
                good = False
                for r in rules:
                    if check(k, r):
                        good = True
                        break
                if not good:
                    tot += k
                    valid = False
            if valid:
                near.append(list(map(int, j.split(","))))
    else:
        for j in s:
            a = re.split(r": | or |-", j)
            rules.append([*map(int, a[1:])])

print(tot)
# print(near)
real = {i: set() for i in range(len(rules))}

for idx, r in enumerate(rules):
    for i in range(len(near[0])):
        works = True
        for t in near:
            if not check(t[i], r):
                works = False
                break
        if works:
            real[idx].add(i)

final = [-1] * len(rules)
real = sorted(real.items(), key=lambda x: len(x[1]))
seen = set()
for i in real:
    g = list(i[1] - seen)[0]
    seen.add(g)
    final[i[0]] = g
print(final)

s = my.split(",")
tot = 1
for i in range(6):
    tot *= int(s[final[i]])
print(tot)