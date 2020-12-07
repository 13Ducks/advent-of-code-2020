from aocd import get_data

data = get_data(day=7).split("\n")

c = {}
for i in data:
    s = i.split("contain")
    k = " ".join(s[0].strip().split(" ")[:-1])
    c[k] = list(
        map(lambda x: " ".join(x.strip().split(" ")[:-1]), s[1][:-1].split(","))
    )

cnt = 0
q = ["shiny gold"]
seen = set(["shiny gold"])
while q:
    curr = q.pop(0)
    for k, v in c.items():
        if any(curr in i for i in v):
            if k not in seen:
                cnt += 1
                q.append(k)
                seen.add(k)
print(cnt)


def part2(curr):
    total = 0
    for i in c[curr]:
        spl = i.split(" ")
        n = spl[0].strip()
        b = " ".join(spl[1:]).strip()
        if n.isdigit():
            total += int(n) + int(n) * part2(b)
    return total


print(part2("shiny gold"))