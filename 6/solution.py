

def input():
    with open("6/input.txt", "r") as f:
        groups = f.read().split("\n\n")
    return [group.split("\n") for group in groups]

def test_input():
    groups = """abc

a
b
c

ab
ac

a
a
a
a

b""".strip().split("\n\n")

    return [group.split("\n") for group in groups]


def sol1():
    groups = input()
    #print("groups: ", groups)
    sum = 0
    for group in groups:
        sum += n_from_group(group)
    return sum

def sol2():
    groups = input()
    #print("groups: ", groups)
    sum = 0
    for group in groups:
        sum += n_from_group2(group)
    return sum


def n_from_group(group):
    sum = 0
    yes = []
    for ans in group:
        sum = 0
        for c in ans.strip():
            if c not in yes:
                yes.append(c)
        sum += len(yes)
    return sum

def n_from_group2(group):
    sum = 0
    yes = []
    for ans in group:
        sum = 0
        for c in ans.strip():
            yes.append(c)
    checked = []
    for y in yes:
        if y not in checked:
            checked.append(y)
            if yes.count(y) == len(group):
                sum += 1
    return sum


print(sol1())
print(sol2())