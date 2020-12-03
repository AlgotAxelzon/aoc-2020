import re
f = open("input.txt", "r")

text = f.read()

str_numbers = re.findall("[0-9]+", text)
numbers = [int(s) for s in str_numbers]

for i in range(0,len(numbers)):
    for j in range(i+1, len(numbers)):
        if (numbers[i] + numbers[j] == 2020):
            print("Part One: ", numbers[i]*numbers[j])
        for k in range(j+1, len(numbers)):
            if (numbers[i] + numbers[j] + numbers[k] == 2020):
                print("Part Two: ", numbers[i]*numbers[j]*numbers[k])

print("done")
