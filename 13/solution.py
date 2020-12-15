def input():
    with open("13/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def test_input():
    return """939
17,x,13,19""".split("\n")

def sol1():
    lines = input()
    goal = int(lines[0])
    bus_ids = [int(x) for x in lines[1].split(",") if x != "x"]
    closest = (0, 99999)

    for id in bus_ids:
        _, o = divmod(goal, id)
        minutes = id - o
        if minutes < closest[1]:
            closest = (id, minutes)
    return closest[0]*closest[1]

def sol2():
    return

print(sol1())
print(sol2())