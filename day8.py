from aocd import get_data

data = get_data(day=8).split("\n")


def run_console(data):
    ptr = 0
    acc = 0
    seen = set()
    while True:
        if ptr in seen:
            return (acc, False)
        if ptr > len(data) - 1:
            return (acc, True)
        seen.add(ptr)
        op, arg = data[ptr].split()
        if op == "nop":
            ptr += 1
        elif op == "acc":
            acc += int(arg)
            ptr += 1
        elif op == "jmp":
            ptr += int(arg)


print(run_console(data)[0])
for i, v in enumerate(data):
    s = v.split()
    if s[0] == "acc":
        continue
    new_data = data.copy()
    new_data[i] = ("nop" if s[0] == "jmp" else "jmp") + " " + s[1]
    ret = run_console(new_data)
    if ret[1]:
        print(ret[0])
        break
