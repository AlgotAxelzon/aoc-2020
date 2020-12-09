def input():
    with open("9/input.txt", "r") as f:
        return [s[:-1] for s in f.readlines()]

def sol1():
    n_preamble = 25
    numbers = [int(x) for x in input()]

    for i in range(n_preamble,len(numbers)):
        five_prev = numbers[i-n_preamble:i+1]
        found = False
        for n in range(0,n_preamble):
            for k in range(n+1,n_preamble):
                if int(five_prev[n]) + int(five_prev[k]) == int(five_prev[n_preamble]):
                    found = True
                    break
        if not found:
            return five_prev[n_preamble]


def sol2():
    wanted = int(sol1())
    numbers = [int(x) for x in input()]

    ns = []

    for i in range(0,len(numbers)):
        for width in range(2+1,len(numbers)+1):
            if (i+width) > len(numbers):
                continue
            if sum(numbers[i:i+width-1]) == wanted:
                ns = numbers[i:i+width-1]
                break
    
    print(ns)
    return max(ns) + min(ns)


print(sol1())
print(sol2())