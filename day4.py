from aocd import get_data
import re

data = get_data(day=4)
data = list(map(lambda x: re.split(" |\n", x), data.split("\n\n")))

cnt1 = cnt2 = 0

for p in data:
    if len(p) <= 6:
        continue
    valid1 = valid2 = True
    for e in p:
        f, v = e.split(":")
        if len(p) == 7 and f == "cid":
            valid1 = False
            valid2 = False
        if f == "byr" and not (1920 <= int(v) <= 2002):
            valid2 = False
        if f == "iyr" and not (2010 <= int(v) <= 2020):
            valid2 = False
        if f == "eyr" and not (2020 <= int(v) <= 2030):
            valid2 = False
        if f == "hgt":
            n = v[:-2]
            if v.endswith("cm") and not (150 <= int(n) <= 193):
                valid2 = False
            if v.endswith("in") and not (59 <= int(n) <= 76):
                valid2 = False
            if not ("cm" in v or "in" in v):
                valid2 = False
        if f == "hcl":
            a = [i for i in v[1:] if i in "abcdef0123456789"]
            if not (v[0] == "#" and len(a) == 6 and len(v) == 7):
                valid2 = False
        if f == "ecl" and not (v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            valid2 = False
        if f == "pid" and not (v.isnumeric() and len(v) == 9):
            valid2 = False

    if valid1:
        cnt1 += 1
    if valid2:
        cnt2 += 1

print(cnt1, cnt2)