from aocd import get_data
import math

data = get_data(day=12).split("\n")

curr_angle = 0
pos1 = [0, 0]
pos2 = [0, 0]
waypoint = [10, 1]
dirs = {"N": 90, "W": 180, "S": 270, "E": 0}

for v in data:
    d = v[0]
    a = int(v[1:])

    if d == "F":
        pos1[0] += round(math.cos(curr_angle) * a)
        pos1[1] += round(math.sin(curr_angle) * a)
        pos2[0] += waypoint[0] * a
        pos2[1] += waypoint[1] * a
    elif d in dirs:
        ang = math.radians(dirs[d])
        pos1[0] += round(math.cos(ang) * a)
        pos1[1] += round(math.sin(ang) * a)
        waypoint[0] += round(math.cos(ang)) * a
        waypoint[1] += round(math.sin(ang)) * a
    else:
        a_r = math.radians(a)
        if d == "L":
            curr_angle += math.radians(a)
        else:
            curr_angle -= math.radians(a)
            a_r = -a_r

        x, y = waypoint
        x_p = round(x * math.cos(a_r) - y * math.sin(a_r))
        y_p = round(y * math.cos(a_r) + x * math.sin(a_r))
        waypoint = [x_p, y_p]

print(abs(pos1[0]) + abs(pos1[1]))
print(abs(pos2[0]) + abs(pos2[1]))