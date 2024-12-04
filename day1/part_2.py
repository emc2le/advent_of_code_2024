line = []

with open("input.txt") as f:
    for l in f:
        line.append(l)


liste1 = []
liste2 = []

for l in line:
    liste1.append(int(l[0:l.find(" ")]))
    liste2.append(int(l[l.find(" ")+3:len(l)-0].replace("\n", "")))

score = 0
for x in liste1:
    score+=x*liste2.count(x)

print(score)