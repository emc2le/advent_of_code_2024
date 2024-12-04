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

def test_si_fonctionne(report):
    reverse_report = report.copy()
    sort_report = report.copy()

    sort_report.sort()
    reverse_report.sort(reverse=True)

    if report == sort_report or report==reverse_report:
        for i in range(1, len(report)):
            if not(-3<=report[i]-report[i-1]<=3) or (report[i]-report[i-1]) == 0:
                return False
        return True
    
    else:
        return False

count=0
for report in data:
    if test_si_fonctionne(report):
        count+=1
    else:
        for e in range(0, len(report)):
            report_copy = report.copy()
            del(report_copy[e])
            if test_si_fonctionne(report_copy):
                count+=1
                break

print(count)