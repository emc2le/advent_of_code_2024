data = []

with open("input.txt") as f:
    for l in f:
        data.append(l.replace("\n", ""))
        data = data[0]

disk = []
disk_dik = {}

ind = 0
ind_2 = 0
for c_ind in range(0, len(data)):
    if c_ind%2 == 0:
        disk_dik[ind] = int(data[c_ind])
        disk.append([str(ind) for _ in range(int(data[c_ind]))])
        grand = str(ind)
        ind+=1
    else:
        disk.append(["" for _ in range(int(data[c_ind]))])

    ind_2+=1

import os
for id_ordre in range (0, int(grand)+1):
    os.system("cls")
    print(f"{(id_ordre/int(grand)*100)}%")

    id_now = int(grand)-id_ordre
    taille = disk_dik[id_now]

    for x in range(0, len(disk)):
        if disk[x]!=[]:
            if disk[x][0] == "":
                if len(disk[x]) >= taille:
                    # del initial number
                    ind_base_liste_number = disk.index([str(id_now) for _ in range(taille)])
                    if x>ind_base_liste_number:
                        break

                    list_number = disk[ind_base_liste_number].copy()
                    del disk[ind_base_liste_number]
                    disk.insert(ind_base_liste_number, ["" for _ in range(taille)])

                    len_vide = len(disk[x])
                    disk.insert(x, list_number)
                    del disk[x+1]
                    if len_vide-taille != 0:
                        disk.insert(x+1, ["" for _ in range(len_vide-taille)])

                    break

total = 0
ind_total = 0
for l in disk:
    if len(l) != 0:
        if l[0]!="":
            for c in l:
                total+=int(c)*ind_total
                ind_total+=1
        else:
            for _ in l:
                ind_total+=1
print(total)