from aocd import get_data
from itertools import product
import re

data = get_data(day=14).split("\n")

curr_mask = None
mem = {}
for i in data:
    s = i.split(" = ")
    if s[0] == "mask":
        curr_mask = s[1]
        continue

    add = re.split(r"\[|\]", s[0])[1]
    b = list(str(bin(int(s[1])))[2:].zfill(36))
    for i, c in enumerate(curr_mask):
        if c != "X":
            b[i] = c
    n = int("".join(b), 2)
    mem[add] = n

print(sum(mem.values()))

curr_mask = None
mem = {}
for i in data:
    s = i.split(" = ")
    if s[0] == "mask":
        curr_mask = s[1]
        continue

    add = int(re.split(r"\[|\]", s[0])[1])
    b = list(str(bin(add))[2:].zfill(36))
    for i, c in enumerate(curr_mask):
        if c != "0":
            b[i] = c
    v = int(s[1])
    masked = "".join(b)
    perms = list(product(["0", "1"], repeat=masked.count("X")))
    for p in perms:
        curr_n = masked
        for c in p:
            curr_n = curr_n.replace("X", c, 1)
        mem[int(curr_n, 2)] = v

print(sum(mem.values()))
