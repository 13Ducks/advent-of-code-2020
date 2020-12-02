from aocd import get_data

data = get_data(day=2).split("\n")

cnt1 = 0
cnt2 = 0
for i in data:
    r, c, s = i.split(" ")
    c = c[0]
    l, u = map(int, r.split("-"))

    if l <= s.count(c) <= u:
        cnt1 += 1

    if (s[l - 1] == c) ^ (s[u - 1] == c):
        cnt2 += 1

print(cnt1, cnt2)
