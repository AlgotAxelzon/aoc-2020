from math import cos, sin, pi

def input():
    with open("12/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def instruction1(line, pos):
    a = line[0]
    if a == "N":
        pos[2] += int(line[1:])
    if a == "S":
        pos[2] -= int(line[1:])
    if a == "E":
        pos[1] += int(line[1:])
    if a == "W":
        pos[1] -= int(line[1:])
    if a == "L":
        pos[0] += int(line[1:])
    if a == "R":
        pos[0] -= int(line[1:])
    if a == "F":
        pos[1] += int(line[1:])*cos(pi / 180 * pos[0])
        pos[2] += int(line[1:])*sin(pi / 180 * pos[0])
    return pos

def rotate(pos, angle):
    angle = angle * pi / 180
    px, py = pos[0], pos[1]

    qx = cos(angle) * px - sin(angle) * py
    qy = sin(angle) * px + cos(angle) * py
    return [qx, qy]

def instruction2(line, ship, wp):
    a = line[0]
    if a == "N":
        wp[1] += int(line[1:])
    if a == "S":
        wp[1] -= int(line[1:])
    if a == "E":
        wp[0] += int(line[1:])
    if a == "W":
        wp[0] -= int(line[1:])
    if a == "L":
        wp = rotate(wp, int(line[1:]))
    if a == "R":
        wp = rotate(wp, -int(line[1:]))
    if a == "F":
        ship[0] += wp[0] * int(line[1:])
        ship[1] += wp[1] * int(line[1:])
    return ship, wp

def manhattan(x, y):
    return abs(x) + abs(y)

def sol1():
    lines = input()

    pos = [0,0,0]

    for line in lines:
        pos = instruction1(line, pos)

    return round(manhattan(pos[1],pos[2]))

def sol2():
    lines = input()

    ship = [0,0]
    wp = [10,1]

    for line in lines:
        ship, wp = instruction2(line, ship, wp)

    return round(manhattan(ship[0],ship[1]))

print(sol1())
print(sol2())