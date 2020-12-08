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
            return acc, visited

def sol2():
    _, change = sol1()
    switch = ['nop', 'jmp']
    for i in range(0,2):
        for n in change:
            instrs = [parse_line(instr) for instr in input()]
            if instrs[n][0] != switch[i]:
                continue
            acc = 0
            visited = []
            pc = 0
            while True:
                acc, visited, pc = ex_op(instrs[pc], acc, visited, pc)
                if pc == n:
                    instrs[pc] = [switch[i-1], instrs[pc][1]] 
                if pc == len(instrs):
                    return acc, "ended correctly"
                if pc in visited:
                    break
    return "only loops"

print(sol1()[0])
print(sol2()[0])