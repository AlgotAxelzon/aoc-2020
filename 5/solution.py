import math

def seatId(string):
    rows = [0, 127]
    cols = [0, 7]
    for c in string:
        if c == "F":
            rows[1] = math.floor((rows[0] + rows[1]) / 2)
        if c == "B":
            rows[0] = math.ceil((rows[0] + rows[1]) / 2)
        if c == "L":
            cols[1] = math.floor((cols[0] + cols[1]) / 2)
        if c == "R":
            cols[0] = math.ceil((cols[0] + cols[1]) / 2)
    return rows[0]*8 + cols[0]

def get_lines():
    with open("5/input.txt", "r") as f:
        lines = f.readlines()
    return [line for line in lines]

def sol1():
    booked = [seatId(string) for string in get_lines()]
    return max(booked)

def sol2():
    booked = sorted([seatId(string) for string in get_lines()])

    all_seats = list(range(0,(127*8)+8))

    avalible_seats = [seat for seat in all_seats if seat not in booked]

    for seat in avalible_seats:
        if (seat+1 not in avalible_seats) and (seat-1 not in avalible_seats):
            return seat


print(sol1())
print(sol2())




