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
            guardian=[number_line, number_colomn]
            direction = map[number_line][number_colomn]
            cont=False
            break
    if cont == False:
        break

guardin_list_position = []
guardin_list_position.append(guardian.copy())

map[guardian[0]][guardian[1]] = "."

while True:
    if direction=="^":
        if guardian[0]-1 >= 0:
            if map[guardian[0]-1][guardian[1]] == "#":
                direction=">"
            else:
                guardian[0] -=1
        else:
            break
            
    elif direction=="v":
        if guardian[0]+1 < dimension[0]:
            if map[guardian[0]+1][guardian[1]] == "#":
                direction="<"
            else:
                guardian[0] +=1
        else:
            break

    elif direction==">":
        if guardian[1]+1 < dimension[1]:
            if map[guardian[0]][guardian[1]+1] == "#":
                direction="v"
            else:
                guardian[1] +=1
        else:
            break


    elif direction=="<":
        if guardian[1]-1 >= 0:
                if map[guardian[0]][guardian[1]-1] == "#":
                    direction="^"
                else:
                    guardian[1] -=1
        else:
            break

    if not(guardian in guardin_list_position):
        guardin_list_position.append(guardian.copy())

print(len(guardin_list_position))
