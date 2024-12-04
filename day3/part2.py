import re

data = ""

with open("input.txt") as f:
    for l in f:
        data+=l



positive = re.findall("mul\\((\\d+),(\\d+)\\)", data)

index_dic = {}

ind = 0
do_index = []
while ind!=-1:
    ind = data.find("do()", ind+1)
    do_index.append(ind)
del(do_index[len(do_index)-1])
for e in do_index:
    index_dic[e]="do"


ind = 0
dont_index = []
while ind!=-1:
    ind = data.find("don't()", ind+1)
    dont_index.append(ind)
del(dont_index[len(dont_index)-1])
for e in dont_index:
    index_dic[e]="dont"

index_dic = dict(sorted(index_dic.items()))

index_number = [x for x in index_dic]

positive_str = data[0:index_number[0]]
for k in index_dic:

    if index_dic[k]=="do":
        try:
            positive_str=positive_str + data[k:index_number[index_number.index(k)+1]]
        except:
            positive_str=positive_str  +data[k:len(data)]


total = 0
m = re.findall("mul\\((\\d+),(\\d+)\\)", positive_str)

for c in m:
    total+=int(c[0])*int(c[1])
print(total)