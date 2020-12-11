from aocd import get_data

data = ["." + i + "." for i in get_data(day=11).split("\n")]
data = ["." * len(data[0])] + data + ["." * len(data[0])]

moves = [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (1, 0), (0, 1)]


def next_state(data, count_filled, max_neighbors):
    new_data = []
    for i in range(1, len(data) - 1):
        build = "."
        for j in range(1, len(data[0]) - 1):
            cnt = count_filled(data, i, j)
            if data[i][j] == "L" and cnt == 0:
                build += "#"
            elif data[i][j] == "#" and cnt >= max_neighbors:
                build += "L"
            else:
                build += data[i][j]
        new_data.append(build + ".")
    new_data = ["." * len(new_data[0])] + new_data + ["." * len(new_data[0])]
    return new_data


def adj_count(data, i, j):
    cnt = 0
    for m in moves:
        x, y = m
        if data[i + x][j + y] == "#":
            cnt += 1
    return cnt


def vis_count(data, curr_x, curr_y):
    cnt = 0
    for m in moves:
        x, y = m
        i, j = curr_x, curr_y
        while True:
            i += x
            j += y

            if (i < 0 or i > len(data) - 1) or (j < 0 or j > len(data[0]) - 1):
                break

            if data[i][j] == "#":
                cnt += 1
                break
            elif data[i][j] == "L":
                break
    return cnt


def calc_equil(data, count_filled, max_neighbors):
    states = set()
    combined = ""
    while combined not in states:
        states.add(combined)
        data = next_state(data, count_filled, max_neighbors)
        combined = "".join(data)
    return combined.count("#")


print(calc_equil(data.copy(), adj_count, 4))
print(calc_equil(data.copy(), vis_count, 5))