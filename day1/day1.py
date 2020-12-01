# DAY 1

file = open("day1/day1.txt")
data = list(map(lambda x: int(x.strip()), file.readlines()))

for i in data:
    for j in data:
        if i + j == 2020:
            print(i * j)
        for k in data:
            if i + j + k == 2020:
                print(i * j * k)
