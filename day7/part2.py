import itertools

line = []

with open("input.txt") as f:
    for l in f:
        line.append(l.replace("\n", ""))

result = []
liste_nombre = []

for l in line:
    split = l.split(": ")
    result.append(int(split[0]))
    liste_nombre.append([int(x) for x in split[1].split(" ")])


def is_calculable(liste, result):
    len_liste = len(liste)

    l_pos = []
    for _ in range(len_liste-1):
        l_pos.append(0)
        l_pos.append(1)
        l_pos.append(3)

# Eviter les doublons
    comb = set(itertools.combinations(l_pos,len_liste-1))

    for c in comb:
        total = liste[0]
        for i in range(1, len_liste):
            if total>result:
                break
            if c[i-1] == 0:
                total+=liste[i]
            elif c[i-1] == 1:
                total*=liste[i]
            else:
                total=int(str(total)+str(liste[i]))
        if total == result:
            return True
    return False

total = 0
import os
len_liste_nombre = len(liste_nombre)
for i in range(0, len(liste_nombre)):
    os.system("cls")
    print(f"{(i/len_liste_nombre)*100}%")
    if is_calculable(liste_nombre[i], result[i]):
        total+= result[i]

        
print(total)