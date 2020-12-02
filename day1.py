from aocd import get_data

data = get_data(day=1).split("\n")
data = list(map(lambda x: int(x.strip()), data))

for i in data:
    for j in data:
        if i + j == 2020:
            print(i * j)
        for k in data:
            if i + j + k == 2020:
                print(i * j * k)
