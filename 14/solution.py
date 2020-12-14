def input():
    with open("14/input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def apply_mask(mask, bin_string):
    mask_len = len(mask)
    string_len = len(bin_string)
    mask = [c for c in mask]
    bin_string = [c for c in bin_string]
    for i in range(0, mask_len):
        if (mask[mask_len-1-i]) == "X":
            if string_len-1-i >= 0:
                mask[mask_len-1-i] = bin_string[string_len-1-i]
            else:
                mask[mask_len-1-i] = "0"

        elif (mask[mask_len-1-i]) == "1":
            mask[mask_len-1-i] = "1"

        elif (mask[mask_len-1-i]) == "0":

            mask[mask_len-1-i] = "0"
    return ''.join(mask)

def apply_mask2(mask, addr_str):
    mask_len = len(mask)
    addr_len = len(addr_str)
    mask = [c for c in mask]
    addr_str = [c for c in addr_str]
    for i in range(0, mask_len):
        if (mask[mask_len-1-i]) == "X":
            mask[mask_len-1-i] = "X"

        elif (mask[mask_len-1-i]) == "1":
            mask[mask_len-1-i] = "1"

        elif (mask[mask_len-1-i]) == "0":
            if addr_len-1-i >= 0:
                mask[mask_len-1-i] = addr_str[addr_len-1-i]
            else:
                mask[mask_len-1-i] = "0"
    return ''.join(mask)

def replace_xs(string_w_xs):
    res = [string_w_xs]
    while True in [hasX(c) for c in res]:
        for i in range(0, len(res)):
            if "X" in res[i]:
                replaced = replace_first_x(res[i])
                res[i] = replaced[0]
                res.append(replaced[1])
    return res
    
def hasX(string_w_xs):
    return "X" in string_w_xs

def replace_first_x(string_w_xs):
    list_w_xs = [c for c in string_w_xs]
    for i in range(0, len(list_w_xs)):
        if list_w_xs[i] == "X":
            r1 = list_w_xs.copy()
            r2 = list_w_xs.copy()
            r1[i] = "1"
            r2[i] = "0"
            return [''.join(r1), ''.join(r2)]
    return None

def sol1():
    lines = input()
    mem = dict()
    mask = 0
    for line in lines:
        if line[:4] == "mask":
            mask_b2 = line.split(" = ")[1]
            mask = mask_b2
        elif line[:4] == "mem[":
            args = line.split(" = ")
            addr = args[0][4:-1]
            value_b2 = bin(int(args[1]))[2:]
            masked = apply_mask(mask, value_b2)
            masked_b10 = int(masked, 2)
            mem[addr] = masked_b10
    return sum(mem.values())

def sol2():
    lines = input()
    mem = dict()
    mask = 0
    for line in lines:
        if line[:4] == "mask":
            mask_b2 = line.split(" = ")[1]
            mask = mask_b2
        elif line[:4] == "mem[":
            args = line.split(" = ")
            addr = bin(int(args[0][4:-1]))[2:]
            value_b2 = int(args[1])
            masked_addr = apply_mask2(mask, addr)
            all_addrs = replace_xs(masked_addr)

            all_addrs_b10 = [int(masked, 2) for masked in all_addrs]
            for addr in all_addrs_b10:
                mem[addr] = value_b2
    return sum(mem.values())

print(sol1())
print(sol2())