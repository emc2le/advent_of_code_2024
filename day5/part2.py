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

ouvrage_non_imprime = []
for o in ouvrage:
    for regle in condition:
        if regle[0] in o and regle[1] in o:
            if not(o.index(regle[0]) < o.index(regle[1])):
                ouvrage_non_imprime.append(o)
                break


def test(o):
    for regle in condition:
        if regle[0] in o and regle[1] in o:
            if not(o.index(regle[0]) < o.index(regle[1])):
                return False
    return True

def rearange(o):
    o_rep = o
    while test(o_rep) == False:
        for regle in condition:
            if regle[0] in o_rep and regle[1] in o_rep:
                while not(o_rep.index(regle[0]) < o_rep.index(regle[1])):
                    temp = o_rep[o_rep.index(regle[1])+1]
                    o_rep[o_rep.index(regle[1])+1] = o_rep[o_rep.index(regle[1])] 
                    o_rep[o_rep.index(regle[1])] = temp

    return o_rep


ouvrage_traite = []

for o in ouvrage_non_imprime:
    ouvrage_traite.append(rearange(o))

somme_milieu = 0
for o in ouvrage_traite:
    somme_milieu+=o[int((len(o)-1)/2)]

print(somme_milieu)