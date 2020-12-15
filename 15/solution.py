def input():
    return [2,15,0,9,1,20]

def test_input():
    return [0,3,6]

def sol1(nth):
    start_nums = input()
    dic = dict()
    for i in range(0, len(start_nums)):
        dic[str(start_nums[i])] = [i+1]
    last = start_nums[-1]
    turn = len(start_nums)+1

    while turn <= nth:
        if turn % 1500000 == 0:
            print("turn", turn, "/", nth, turn/nth*100, "%")
        say = 0
        if len(dic[str(last)]) == 1:
            say = 0
        else:
            turns_said = dic[str(last)]
            say = turns_said[-1] - turns_said[-2]
        if str(say) in dic:
            dic[str(say)].append(turn)
        else:
            dic[str(say)] = [turn]
        last = say
        turn += 1
    return last

def sol2():
    return sol1(30000000)

print(sol1(2020))
print(sol2())