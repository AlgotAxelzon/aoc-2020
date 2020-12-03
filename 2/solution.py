import re

def count_character(character, string):
    cnt = 0
    for c in string:
        if c == character:
            cnt += 1
    return cnt

def isPartOneValid(numbers, c, password):
    repeats_in_pass = count_character(c, password)
    if numbers[0] <= repeats_in_pass and repeats_in_pass <= numbers[1]:
        return True
    return False

def isPartTwoValid(numbers, c, password):
    if (password[numbers[0]-1] == c) != (password[numbers[1]-1] == c):
        return True
    return False


f = open("input.txt", "r")

part_one_valid = 0
part_two_valid = 0

line = f.readline()
while line:
    numbers = [int(n) for n in re.findall("[0-9]+", line)]
    character = re.findall("[a-z]\:", line)[0][0]
    password = re.findall("[a-z]+$", line)[0]

    if isPartOneValid(numbers, character, password):
        part_one_valid += 1

    if isPartTwoValid(numbers, character, password):
        part_two_valid += 1

    line = f.readline()

print("Part One: ", part_one_valid)
print("Part Two: ", part_two_valid)

