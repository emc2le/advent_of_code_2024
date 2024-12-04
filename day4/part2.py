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

a=[]

for l in line: 
    a.append(find_character_in_line("A", l))

count_XMAS=0

count_line=0

#line, colomn M, M, S, S
trans = (((-1, -1), (1, -1), (-1, 1), (1, 1)), (((-1, 1), (1, 1), (-1, -1), (1, -1))), ((-1, -1), (-1, 1), (1, -1), (1, 1)), ((1, -1), (1, 1), (-1, -1), (-1, 1)))


for a_line in a:
    for e in a_line:
        try:
            for t in trans: 
                m_1 = line[count_line+t[0][0]][e+t[0][1]]
                m_2 = line[count_line+t[1][0]][e+t[1][1]]
                s_1 = line[count_line+t[2][0]][e+t[2][1]]
                s_2 = line[count_line+t[3][0]][e+t[3][1]]

                if count_line+t[0][0] >=0 and count_line+t[1][0] >= 0 and count_line+t[2][0]>=0 and count_line+t[3][0] >=0 and e+t[0][1] >= 0 and e+t[1][1]>=0 and e+t[2][1] >= 0 and e+t[3][1] >=0:
                    if m_1 == "M" and m_2 == "M" and s_1 == "S" and s_2 =="S":
                        count_XMAS+=1
        except:
            pass
    
    count_line+=1

print(count_XMAS)