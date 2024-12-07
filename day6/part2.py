line = []

with open("input.txt") as f:
    for l in f:
        line.append(l.replace("\n", ""))

map = []
for l in line:
    line_append=[]
    for c in l:
        line_append.append(c)
    map.append(line_append)


dimension = (len(map), len(map[0])) #line, colomn

cont = True
for number_line in range(0, dimension[0]):
    for number_colomn in range(0, dimension[1]):
        if map[number_line][number_colomn]!="." and map[number_line][number_colomn]!="#":
            guardian=(number_line, number_colomn)
            cont=False
            break
    if cont == False:
        break

map[guardian[0]][guardian[1]] = "."

map_tupple=[]
for i in map:
    map_tupple.append(tuple(i))
map = tuple(map_tupple)


def is_blocked(m, max):
    direction = "^"

    pos_guard = list(guardian)
    compt = 0
    while compt<max:
        compt += 1
        
        if direction=="^":
            if pos_guard[0]-1<0:
                return False
            else:
                if m[pos_guard[0]-1][pos_guard[1]] == "#":
                    direction=">"
                else:
                    pos_guard[0] -=1


        elif direction=="v":
            if pos_guard[0]+1>=dimension[0]:
                return False
            else:
                if m[pos_guard[0]+1][pos_guard[1]] == "#":
                    direction="<"
                else:
                    pos_guard[0] +=1

        elif direction==">":
            if pos_guard[1]+1>=dimension[1]:
                return False
            else:
                if m[pos_guard[0]][pos_guard[1]+1] == "#":
                    direction="v"
                else:
                    pos_guard[1] +=1
        elif direction=="<":
            if pos_guard[1]-1<0:
                return False
            else:
                if m[pos_guard[0]][pos_guard[1]-1] == "#":
                    direction="^"
                else:
                    pos_guard[1] -=1

    return True

number = 0
max_val = 1000000

for number_line in range(0, dimension[0]):
    for number_colomn in range(0, dimension[1]):
        if not(number_line==guardian[0] and number_colomn==guardian[1]):
            map2 = []
            for l in map:
                map2.append(list(l))

            if map2[number_line][number_colomn] != "#":
                map2[number_line][number_colomn] = "#"
                if is_blocked(map2, max_val) == True:
                    number+=1

print(number)