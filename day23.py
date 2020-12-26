from aocd import get_data

data = [*map(int, get_data(day=23))]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_cll(p2=False):
    nodes = {}
    prev = None
    for v in data:
        curr = Node(v)
        if prev:
            prev.next = curr
        prev = curr
        nodes[v] = curr

    if p2:
        for i in range(10, 1000001):
            curr = Node(i)
            prev.next = curr
            prev = curr
            nodes[i] = curr

    start = data[0]
    prev.next = nodes[start]
    return start, nodes


def run_game(nodes, start, num_moves):
    max_val = len(nodes)
    for _ in range(num_moves):
        nxt = nodes[start]
        a = nxt.next
        b = a.next
        c = b.next

        dest = start
        while True:
            dest -= 1
            if not dest:
                dest = max_val
            if not dest in (a.data, b.data, c.data):
                break

        dest = nodes[dest]
        nodes[start].next = c.next
        c.next = dest.next
        dest.next = a

        start = nodes[start].next.data

    return nodes[1]


start, nodes = create_cll(False)
s = run_game(nodes, start, 100)
p1 = ""
while True:
    s = s.next
    if s.data == 1:
        break
    p1 += str(s.data)

print(p1)

start, nodes = create_cll(True)
run_game(nodes, start, 10000000)

print(nodes[1].next.data * nodes[1].next.next.data)