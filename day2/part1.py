line = []

with open("input.txt") as f:
    for l in f:
        line.append(l)

data = []
for report in line:
    l = report.replace("\n", "").split(" ")
    l_int = []
    for i in l:
        l_int.append(int(i))

    data.append(l_int)

count=0
for report in data:
    reverse_report = report.copy()
    sort_report = report.copy()

    sort_report.sort()
    reverse_report.sort(reverse=True)

    if report == sort_report or report==reverse_report:

        fonctionne = True
        for i in range(1, len(report)):
            if not(-3<=report[i]-report[i-1]<=3) or (report[i]-report[i-1]) == 0:
                fonctionne=False
                break
        if fonctionne == True:
            count+=1
print(count)