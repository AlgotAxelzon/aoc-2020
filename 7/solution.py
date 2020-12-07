def test_input1():
    return """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split("\n")

def test_input2():
    return """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".split("\n")

import re

def getRule(string):
    bag = string.split("bags")[0].strip()
    bags_str = re.findall(r'[0-9]+ \w+ \w+',string[:-1])
    bags = []
    for thing in bags_str:
        bags.append([thing[:1], thing[2:]])
    return [bag] + bags
            
def input():
    with open("7/input.txt", "r") as f:
        return f.readlines()

def rules_with_bag(bag, rules):
    bag_rules = [rule for rule in rules if bag in [item[1] for item in rule if len(item) == 2 ]]
    return bag_rules

def rules_for_bag(bag, rules):
    return [rule for rule in rules if bag in rule][0]

def n_bags_in_bag(bag, rules):
    rule = rules_for_bag(bag, rules)
    if rule == [bag]:
        return 0
    else:
        return sum([int(bagx[0]) + (int(bagx[0]) * n_bags_in_bag(bagx[1], rules)) for bagx in rule[1:]])

def sol1():
    lines = input()
    rules = [getRule(line) for line in lines]
    checked = []
    todo = []
    todo = [x[0] for x in rules_with_bag("shiny gold", rules)]
    while todo != []:
        bag = todo.pop(0)
        if bag in checked:
            continue
        checked.append(bag)
        bags = [x[0] for x in rules_with_bag(bag, rules)]
        for bag in bags:
            todo.append(bag)
    return len(checked)


def sol2():
    lines = input()
    rules = [getRule(line) for line in lines]
    return n_bags_in_bag("shiny gold", rules)
    

print(sol1())
print(sol2())
