from aocd import get_data
import re

data = get_data(day=18).split("\n")


class Equation:
    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return Equation(self.v + o.v)

    def __sub__(self, o):
        return Equation(self.v * o.v)

    def __mul__(self, o):
        return Equation(self.v + o.v)


def do_homework(p1):
    hw = data.copy()
    s = 0
    for eq in hw:
        eq = re.sub(r"(\d+)", r"Equation(\1)", eq)
        eq = eq.replace("*", "-")
        if not p1:
            eq = eq.replace("+", "*")
        s += eval(eq).v
    return s


print(do_homework(True))
print(do_homework(False))