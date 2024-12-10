import itertools

data = []

with open("input.txt") as f:
    for l in f:
        data.append([x for x in l.replace("\n", "")])

number_line = len(data)
number_colomn = len(data[0])
charactere_dic={}

for l in range(0, number_line):
    for c in range(0, number_colomn):
        if data[l][c] != ".":
            try:
                charactere_dic[data[l][c]].append((l, c))
            except:
                charactere_dic[data[l][c]]=[]
                charactere_dic[data[l][c]].append((l, c))

def antenne(a1_coord, a2_coord, l, c):
    diff_l = a2_coord[0]-a1_coord[0]
    diff_c = a2_coord[1]-a1_coord[1]

    result = []

    l_a = a1_coord[0]
    c_a = a1_coord[1]

    while 0 <= l_a <l and 0 <= c_a <c:
        if not((l_a, c_a) in result):
            result.append((l_a, c_a))
        l_a += diff_l
        c_a += diff_c

    l_a = a1_coord[0]
    c_a = a1_coord[1]

    while 0 <= l_a <l and 0 <= c_a <c:
        if not((l_a, c_a) in result):
            result.append((l_a, c_a))
        l_a -= diff_l
        c_a -= diff_c


    return result

antenne_total = []
for c in charactere_dic:
    comb_i = itertools.combinations(charactere_dic[c], 2)

    for comb in comb_i:
        ant = antenne(comb[0], comb[1], number_line, number_colomn)
        if ant != []:
            for a in ant:
                if not(a in antenne_total):
                    antenne_total.append(a)

print(len(antenne_total))