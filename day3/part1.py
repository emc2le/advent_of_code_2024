import re

line = []

with open("input.txt") as f:
    for l in f:
        line.append(l)

total = 0
for l in line:
    m = re.findall("mul\\((\\d+),(\\d+)\\)", l)
    
    for c in m:
        total+=int(c[0])*int(c[1])

print(total)