line = []

with open("input.txt") as f:
    for l in f:
        line.append(l)


liste1 = []
liste2 = []

for l in line:
    liste1.append(int(l[0:l.find(" ")]))
    liste2.append(int(l[l.find(" ")+3:len(l)-0].replace("\n", "")))

liste1.sort()
liste2.sort()

total=0
for x in range(0, len(liste1)):
    total+=abs(liste1[x]-liste2[x])

print(total)