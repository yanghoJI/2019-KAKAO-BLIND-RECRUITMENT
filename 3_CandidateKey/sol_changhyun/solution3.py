ncr = []

def solution(relation):
    global ncr
    answer = 0
    newl = []

    #행열 변환
    for i in range(len(relation[0])):
        #print("i",i)
        temp = []
        for j in range(len(relation)):
            temp.append(relation[j][i])
        newl.append(temp)

    N = len(relation)
    tupleN = len(relation[0])


    onlyarr = []
    surplus = []
    ind = 1
    #한 개 짜리 후보키 구하기
    for x in newl:
        setrelation = set(x)
        if len(setrelation) == N:
            answer += 1
            onlyarr.append(ind)
            tupleN -= 1
        else :
            surplus.append(x)
        ind += 1
    #print(onlyarr)
    #print(surplus)


    #두 개 이상의 후보키 구하기
    dfs(tupleN,'1')
    dfs(tupleN,'')
    noneless = list(filter(None.__ne__, ncr))

    tupleLen = 2

    for tupleLen in range(tupleLen, N):
        for x in noneless:
            if len(x) == tupleLen:
                newset = set()
                for i in range(len(surplus[0])):
                    newList = surplus[int(x[0])-1][i] + surplus[int(x[1])-1][i]
                    newset.add(newList)
                #print(newset)
                if len(newset) == N:
                    answer += 1
                    onlyarr.append(ind)

    return answer

def dfs(ind, string):
    global ncr
    if ind <= 1:
        return string
    newstring = str(ind)
    ncr.append(dfs(ind - 1, string + newstring))
    ncr.append(dfs(ind - 1, string))

relation = [["100","1","ryan","music","2"],
            ["200","2","apeach","math","2"],
            ["300","3","tube","computer","3"],
            ["400","4","con","computer","4"],
            ["500","5","muzi","music","3"],
            ["600","6","apeach","music","2"]]

#result = 3

#relation = [['100','ryan','music','2'],
#            ['200','apeach','math','1'],
#            ['300','tube','computer','1'],
#            ['400','con','computer','4'],
#            ['500','muzi','music','3'],
#            ['600','apeach','music','2']]

#result = 4

print(solution(relation))
