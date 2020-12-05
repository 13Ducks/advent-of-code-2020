from aocd import get_data
import re

data = get_data(day=4)
data = list(map(lambda x: re.split(" |\n", x), data.split("\n\n")))

cnt1 = cnt2 = 0

for p in data:
    if len(p) <= 6:
        continue
    valid1 = True
    correct2 = 0
    for e in p:
        f, v = e.split(":")
        if len(p) == 7 and f == "cid":
            valid1 = False
        if f == "byr" and 1920 <= int(v) <= 2002:
            correct2 += 1
        if f == "iyr" and 2010 <= int(v) <= 2020:
            correct2 += 1
        if f == "eyr" and 2020 <= int(v) <= 2030:
            correct2 += 1
        if f == "hgt":
            n = v[:-2]
            if v.endswith("cm") and 150 <= int(n) <= 193:
                correct2 += 1
            if v.endswith("in") and 59 <= int(n) <= 76:
                correct2 += 1
        if f == "hcl":
            a = [i for i in v[1:] if i in "abcdef0123456789"]
            if v[0] == "#" and len(a) == 6 and len(v) == 7:
                correct2 += 1
        if f == "ecl" and v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            correct2 += 1
        if f == "pid" and v.isdigit() and len(v) == 9:
            correct2 += 1

    if valid1:
        cnt1 += 1
    if correct2 == 7:
        cnt2 += 1

print(cnt1, cnt2)