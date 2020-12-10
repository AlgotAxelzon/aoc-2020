def input():
    with open("10/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def ways(vals):
    ways_dict = {}
    for val in vals:
        valids = [v for v in vals if 1 <= (val - v) <= 3]
        valids_ways = sum([ways_dict[str(valid)] for valid in valids])
        if val == 1:
            ways_dict[str(val)] = 1
        elif 2 <= val <= 3:
            ways_dict[str(val)] = 1 + valids_ways
        else:
            ways_dict[str(val)] = valids_ways
    return ways_dict[str(max(vals))]

def sol2():
    vals = [int(x) for x in input()]
    vals.sort()
    return ways(vals)

def sol1():
    vals = [int(x) for x in input()]
    vals.sort()

    ones = 0
    threes = 1

    latest_jolt = 0
    for i in range(0, len(vals)):
        if vals[i] -latest_jolt == 1:
            ones += 1
        elif vals[i] -latest_jolt == 3:
            threes += 1
        latest_jolt = vals[i]
    return ones*threes

print(sol1())
print(sol2())
