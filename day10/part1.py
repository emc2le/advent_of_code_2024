line = []

with open("input.txt") as f:
    for l in f:
        l_2 = []
        for x in l.replace("\n", ""):
            l_2.append(int(x))
        line.append(l_2)

pos = {}
for x in range(0, 10):
    pos[x] = []

number_line = len(line)
number_colomn = len(line[0])

for l in range(0, number_line):
    for c in range (0, number_colomn):
        pos[line[l][c]].append((l, c))

def get_neighbour(map, coord):
    trans=[(0, 1), (1, 0), (-1, 0), (0, -1)]
    coords_return = []
    
    elevation = map[coord[0]][coord[1]]
    
    for t in trans:
        l =coord[0]+t[0]
        c= coord[1]+t[1]

        if 0<=l<number_line and 0<=c<number_colomn:
            if map[l][c] == elevation+1:
                coords_return.append((coord[0]+t[0], coord[1]+t[1]))


    return coords_return

coord_0 = []

for l in range(0, number_line):
    for c in range (0, number_colomn):
        if line[l][c] == 0:
            coord_0.append((l, c))
total = 0
for coo in coord_0:
    coord = [coo]
    coord_final = []
    while True:
        if coord == []:
            break
        for c in coord:
            if line[c[0]][c[1]] == 9:
                coord_final.append((c[0], c[1]))
                del coord[coord.index(c)]
            else:
                del coord[coord.index(c)]
                neighbour = get_neighbour(line, c)
                if neighbour!= []:
                    for x in neighbour:
                        coord.append(x)
    coord_final=set(coord_final)
    coord_final_list = list(coord_final)
    total+=len(coord_final_list)

print(total)