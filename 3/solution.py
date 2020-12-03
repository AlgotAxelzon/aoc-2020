f = open("3/input.txt", "r")

directions = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
n_trees = [0, 0, 0, 0, 0]
positions = [[0,0], [0,0], [0,0], [0,0], [0,0]]

line = f.readline()

while line:
    for n in range(0,len(directions)):
        direction = directions[n]
        position = positions[n]

        if (position[1] % direction[1] == 0):
            if (line[position[0]] == "#"):
                n_trees[n] += 1
            positions[n][0] = (position[0] + direction[0]) % (len(line)-1)
        positions[n][1] += 1
    
    #print(positions)
    line = f.readline()

product = 1
for n in n_trees:
    product *= n

print(n_trees)
print(product)
