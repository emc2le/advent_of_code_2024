line = []

with open("input.txt") as f:
    for l in f:
        line.append(l.replace("\n", ""))

def find_character_in_line(ch, line):
    rep = []
    ind = 0
    len_line = len(line)
    
    # Belek
    while len_line!=ind:
        f = line.find(ch, ind)
        if f != -1 and not(f in rep):
            rep.append(f)

        ind+=1

    return rep

x=[]

for l in line: 
    x.append(find_character_in_line("X", l))


count_XMAS=0

count_line=0
trans = ((0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))  #line, colomn

for x_line in x:
    for e in x_line:
        for t in trans:
            try:
                m = line[count_line+t[0]][e+t[1]]
                a = line[count_line+2*(t[0])][e+2*(t[1])]
                s = line[count_line+3*(t[0])][e+3*(t[1])]
                if count_line+t[0]>=0 and e+t[1] >= 0 and count_line+2*(t[0]) >= 0 and e+2*(t[1])>= 0 and count_line+3*(t[0]) >= 0 and e+3*(t[1]) >= 0:
                    if m == "M" and a == "A" and s == "S":
                        count_XMAS+=1
            except:
                pass
    
    count_line+=1

print(count_XMAS)