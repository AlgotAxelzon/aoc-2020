def input():
    with open("11/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def is_occupied(x, y, lines):
    if lines[x][y] == "#":
        return True
    return False

def is_floor(x, y, lines):
    if lines[x][y] == ".":
        return True
    return False

def countNeigbors(lines):
    height = len(lines)
    width = len(lines[0])
    ns = [[0 for x in range(width)] for y in range(height)]
    for i in range(0, height):
        for j in range(0, width):
            if lines[i][j] == ".":
                continue
            neighbours = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i+x < 0 or j+y < 0 or i+x >= height or j+y >= width:
                        continue
                    row = (i + x) 
                    col = (j + y)
                    
                    if is_occupied(row, col, lines):
                        neighbours += 1
            ns[i][j] = neighbours
    return ns

def countNeigbors2(lines):
    height = len(lines)
    width = len(lines[0])
    ns = [[0 for x in range(width)] for y in range(height)]
    for i in range(0, height):
        for j in range(0, width):
            if lines[i][j] == ".":
                continue
            neighbours = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    n = 1
                    while True:
                        row = (i + x*n) 
                        col = (j + y*n)
                        if row < 0 or col < 0 or row >= height or col >= width:
                            break
                        if is_floor(row, col, lines):
                            n += 1
                            continue
                        elif is_occupied(row, col, lines):
                            neighbours += 1
                            break
                        else:
                            break
            ns[i][j] = neighbours
    return ns

def update_board(last_state, ns, x):
    height = len(last_state)
    width = len(last_state[0])
    new_state = [[0 for x in range(width)] for y in range(height)]

    for i in range(0, height):
        for j in range(0, width):
            if last_state[i][j] == ".":
                new_state[i][j] = "."
            elif last_state[i][j] == "L" and ns[i][j] == 0:
                new_state[i][j] = "#"
            elif last_state[i][j] == "#" and ns[i][j] >= x:
                new_state[i][j] = "L"
            else:
                new_state[i][j] = last_state[i][j]
            
    return new_state

def count_occupied(state):
    height = len(state)
    width = len(state[0])
    count = 0

    for i in range(0, height):
        for j in range(0, width):
            if is_occupied(i, j, state):
                count += 1
    return count

def is_same(old, new):
    height = len(old)
    width = len(old[0])
    for i in range(0, height):
        for j in range(0, width):
            if new[i][j] != old[i][j]:
                return False
    return True

def sol1():
    lines = input()
    formated = [[c for c in line] for line in lines]
    last_state = formated

    ns = countNeigbors(last_state)
    new_state = update_board(last_state, ns, 4)

    while not is_same(last_state, new_state):
        last_state = new_state
        ns = countNeigbors(last_state)
        new_state = update_board(last_state, ns, 4)

    return count_occupied(new_state)

def sol2():
    lines = input()
    formated = [[c for c in line] for line in lines]
    last_state = formated

    ns = countNeigbors2(last_state)
    new_state = update_board(last_state, ns, 5)

    while not is_same(last_state, new_state):
        last_state = new_state
        ns = countNeigbors2(last_state)
        new_state = update_board(last_state, ns, 5)

    return count_occupied(new_state)

print(sol1())
print(sol2())