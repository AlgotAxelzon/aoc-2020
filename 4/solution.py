import re
f = open("4/input.txt", "r")

n_valid = 0

passports = f.read().split("\n\n")
for passport in passports:
    pass_formated = re.split(" |\n", passport.strip())
    hasCid = False
    valid = True
    for field in pass_formated:
        value = field[4:]
        if ("byr:" == field[:4]):
            year = int(value)
            if not(1920 <= year and year <= 2002) or not(len(value) == 4):
                print("byr")
                valid = False
        elif ("iyr:" == field[:4]):
            year = int(value)
            if not(2010 <= year and year <= 2020) or not(len(value) == 4):
                print("iyr")
                valid = False
        elif ("eyr:" == field[:4]):
            year = int(value)
            if not(2020 <= year and year <= 2030) or not(len(value) == 4):
                print("eyr")
                valid = False
        elif ("hgt:" == field[:4]):
            if (value[-2:] == "cm"):
                if not(150 <= int(value[:-2]) and int(value[:-2]) <= 193):
                    print("hgt cm")
                    valid = False
            elif (value[-2:] == "in"):
                if not(59 <= int(value[:-2]) and int(value[:-2]) <= 76):
                    print("hgt in")
                    valid = False
            else:
                print("hgt")
                valid = False
        elif ("hcl:" == field[:4]):
            hex = value[1:]
            if not(value[0] == "#" and (re.findall("[a-f0-9]+", hex) != []) and len(hex) == 6):
                print("hcl")
                valid = False
        elif ("ecl:" == field[:4]):
            if not(re.findall("amb|blu|brn|gry|grn|hzl|oth", field) != []):
                print("ecl")
                valid = False
        elif ("pid:" == field[:4]):
            pid = re.findall("[0-9]+", field[4:])
            isNumber = pid != []
            hasLength = False
            if isNumber:
                hasLength = len(pid[0]) == 9
            if not(isNumber and hasLength):
                print("pid")
                valid = False
        elif ("cid:" == field[:4]):
            print("cid")
        else:
            print("else")
            valid = False

        if ("cid:" == field[:4]):
            hasCid = True
            
    if valid and ((len(pass_formated) == 8 and hasCid) or (len(pass_formated) == 7 and (not hasCid))):
        n_valid += 1
        print("v")
    print(pass_formated)

print(n_valid)