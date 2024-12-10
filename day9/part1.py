data = []

with open("input.txt") as f:
    for l in f:
        data.append(l.replace("\n", ""))
        data = data[0]

disk = []

ind = 0
ind_2 = 0
for c_ind in range(0, len(data)):
    if c_ind%2 == 0:
        for _ in range(0, int(data[c_ind])):
            disk.append(str(ind))
        ind+=1
    else:
        for _ in range(0, int(data[c_ind])):
            disk.append("")
    ind_2+=1

import os
for c_ind in range(0, len(disk)):
    os.system("cls")
    print(f"{(c_ind/len(disk))*100}%")
    if disk[c_ind] == "":
        ind_2 = len(disk)-1
        while disk[ind_2] == "" and ind_2>c_ind:
            ind_2-=1
        if ind_2+1 == c_ind:
            break
        disk[c_ind] = disk[ind_2]
        disk[ind_2] = ""

total = 0
ind = 0
for x in disk:
    if x=="":
        break
    total+=int(x)*ind
    ind+=1


print(total)
