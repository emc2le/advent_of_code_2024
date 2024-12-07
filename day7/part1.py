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

# def supprimer_doublons(liste):
#     ind = 0
#     for e in liste:
#         if e in liste[ind+1:]:
#             del liste[ind]
#         ind+=1
#     return liste

def is_calculable(liste, result):
    len_liste = len(liste)

    l_pos = []
    for _ in range(len_liste-1):
        l_pos.append(0)
        l_pos.append(1)

    # Faire attention la combinaison se réalise 2 fois si pas de supprimer doublons
    # Leak mémoire potentiel avec supprimer doublons

    # comb = supprimer_doublons([x for x in itertools.combinations(l_pos,len_liste-1)])
    comb = itertools.combinations(l_pos,len_liste-1)

    for c in comb:
        total = liste[0]
        for i in range(1, len_liste):
            if c[i-1] == 0:
                total+=liste[i]
            else:
                total*=liste[i]
        if total == result:
            return True
    return False

total = 0
import os
for i in range(0, len(liste_nombre)):
    if is_calculable(liste_nombre[i], result[i]):
        total+= result[i]
        os.system("cls")
        print(f"{(i/len(liste_nombre))*100}%")
        
print(total)