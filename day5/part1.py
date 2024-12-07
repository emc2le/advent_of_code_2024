import re

line = []
line_condition = []
line_ouvrage = []

with open("input.txt") as f:
    for l in f:
        line.append(l.replace("\n", ""))
    
    i=0
    while line[i] != "":
        line_condition.append(line[i])
        i+=1
    i+=1
    while i<len(line):
        line_ouvrage.append(line[i])
        i+=1

condition = []
for c in line_condition:
    condition.append([int(x) for x in re.findall(r"(\d+)\|(\d+)",c)[0]])

ouvrage = []
for l in line_ouvrage:
    ouvrage.append([int(x) for x in re.split(",",l)])

ouvrage_imprime = []
for o in ouvrage:
    for regle in condition:
        ajoute = True
        if regle[0] in o and regle[1] in o:
            if not(o.index(regle[0]) < o.index(regle[1])):
                ajoute = False
                break
    if ajoute == True:
        ouvrage_imprime.append(o)

somme_milieu = 0
for o in ouvrage_imprime:
    somme_milieu+=o[int((len(o)-1)/2)]

print(somme_milieu)

