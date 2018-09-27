from itertools import combinations as cb


# set input
indata1 = [['100','ryan','music','2'],['200','apeach','math','2'],['300','tube','computer','3'],['400','con','computer','4'],['500','muzi','music','3'],['600','apeach','music','2']]
indata2 = [['100','ryan','music','2'],['200','apeach','math','1'],['300','tube','computer','1'],['400','con','computer','4'],['500','muzi','music','3'],['600','apeach','music','2']]
result1 = 2
result2 = 3
indata = indata1
result = result1
numOfCol = len(indata[0])

# make checkF
def checkF(table, colindex):
    checklist = []
    for rowdata in table:
        st = ''
        for index in colindex:
            st += rowdata[index]
        checklist.append(st)

    if len(checklist) == len(set(checklist)):
        return colindex
    else:
        return None

# extract combinations and sol
now_col = list(range(numOfCol))
sol = []
removeset = set()

combi = list(cb(now_col, 1))
for x in combi:
    if checkF(indata, x) is not None:
        sol.append(x)
        for k in x:
            if k in now_col:
                now_col.remove(k)

for i in range(2, numOfCol+ 1):
    combi = list(cb(now_col, i))
    for x in combi:
        flag = True
        for ckey in sol:
            if set(ckey) & set(x) == set(ckey):
                flag = False
                break
        if (checkF(indata, x) is not None) and (flag == True):
            sol.append(x)
            if i == 1:
                for k in x:
                    if k in now_col:
                        now_col.remove(k)
    if i > len(now_col):
        break

print(sol)
print('prediction : {}\t\t solution : {}'.format(len(sol), result))

