def input():
    with open("8/input.txt", "r") as f:
        return f.readlines()

def parse_line(string):
    ret = string.split(" ")
    ret = [ret[0], int(ret[1])]
    return ret

def ex_op(instr, acc, visited, pc):
    visited_ret = visited + [pc]
    if instr[0] == "acc":
        return acc+instr[1], visited_ret, pc+1
    elif instr[0] == "jmp":
        return acc, visited_ret, pc+instr[1]
    elif instr[0] == "nop":
        return acc, visited_ret, pc+1

def sol1():
    instrs = [parse_line(instr) for instr in input()]
    acc = 0
    visited = []
    pc = 0
    while True:
        acc, visited, pc = ex_op(instrs[pc], acc, visited, pc)
        if pc in visited:
            return acc, visited[-1]

def sol2():
    _, change = sol1()
    instrs = [parse_line(instr) for instr in input()]
    acc = 0
    visited = []
    pc = 0
    while True:
        acc, visited, pc = ex_op(instrs[pc], acc, visited, pc)
        if pc == change:
            instrs[pc] = ['nop', instrs[pc][1]] 
        if pc == len(instrs):
            return acc, "ended correctly"
        if pc in visited:
            return acc, max(visited)

print(sol1())
print(sol2())