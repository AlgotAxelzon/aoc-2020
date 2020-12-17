import re

def input():
    with open("16/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def ns_in_ranges(dic, numbers):
    bools = numbers.copy()
    for n in range(0, len(numbers)):
        for d in dic:
            for r in dic[d]:
                if r[0] <= int(numbers[n]) <= r[1]:
                    bools[n] = True
        if bools[n] != True:
            bools[n] = False
    return all(bools)

def ns_in_range(dic, d, numbers):
    bools = numbers.copy()
    for n in range(0, len(numbers)):
        for r in dic[d]:
            if r[0] <= int(numbers[n]) <= r[1]:
                bools[n] = True
        if bools[n] != True:
            bools[n] = False
    return all(bools)

def n_in_range(dic, number):
    for d in dic:
        for r in dic[d]:
            if r[0] <= int(number) <= r[1]:
                return True
    return False

def sol():
    lines = input()
    dic = dict()
    
    for line in lines:
        ranges = re.findall('[0-9]+\-[0-9]+', line)
        if len(ranges) > 0:
            field = line.split(":")[0]
            dic[field] = []
            for rang in ranges:
                dic[field].append([int(x) for x in rang.split("-")])

    is_your = -1
    nearby = []
    your = []

    for i in range(0, len(lines)):
        if i == is_your:
            your = lines[i].split(",")
        if lines[i] == "your ticket:":
            is_your = i+1
        if lines[i] == "nearby tickets:":
            continue
        if lines[i] == "":
            continue
        if len(lines[i].split(",")) > 1:
            nearby.append(lines[i].split(","))

    valid = []
    invalid = []

    for i in range(0, len(nearby)):
        if ns_in_ranges(dic, nearby[i]):
            valid.append(nearby[i])
        else:
            invalid.append(nearby[i])

    sum = 0

    for i in invalid:
        for n in i:
            if not n_in_range(dic, n):
                sum += int(n)
    print("part 1:", sum)

    fits = dict()

    for f in range(0, len(valid[0])):
        values = []
        for t in range(0, len(valid)):
            values.append(valid[t][f])
        for d in dic:
            field_valid = []
            field_valid.append(ns_in_range(dic, d, values))
            if all(field_valid):
                if d in fits:
                    fits[d].append(f)
                else:
                    fits[d] = [f]

    avalible = list(range(0,len(your)))
    used = []
    pax = dict()

    while avalible != []:
        for d in fits:
            if len(fits[d]) == 1 and fits[d] != []:
                use = fits[d][0]
                used.append(use)
                pax[d] = use
                avalible.remove(use)
                fits[d].remove(use)
                for d2 in fits:
                    if d2 != d:
                        if use in fits[d2]:
                            fits[d2].remove(use)

    product = 1

    for p in pax:
        if "departure" in p:
            product *= int(your[pax[p]])
    print("part 2:", product)

sol()