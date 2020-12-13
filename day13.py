from aocd import get_data
from functools import reduce

data = get_data(day=13).split("\n")

# CHINESE REMAINDER THEOREM from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python


def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    return s % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


min_t = int(data[0])
times = []
num = []
rem = []

for i, v in enumerate(data[1].split(",")):
    if v != "x":
        n = int(v)
        d = (min_t // n + 1) * n - min_t
        times.append((n, d))

        num.append(n)
        rem.append((n - i) % n)

best = min(times, key=lambda x: x[1])
print(best[0] * best[1])
print(chinese_remainder(num, rem))