def solution(N,stages):
    status = [0] * (N+2)
    sum = 0

    #stage 도달 수
    for x in stages:
        status[x] += 1

    #sum
    for i in range(len(status)):
        sum += status[i]

    #계산 작업
    proc = dict()
    i=1
    for y in status[1:-1]:
        proc[i] = y/sum
        sum -= y

        i+=1

    #정렬
    answer = []
    for y, v in sorted(proc.items(), key=lambda proc: proc[1],reverse=True):
        answer.append(y)
    #print(sorted_list, proc)
    return answer


## 1

N = 5
stages = [2,1,2,6,2,4,3,3]
##result = [3,4,2,1,5]


## 2

#N = 4
#stages = [4,4,4,4,4]
##result = [4,1,2,3]


print(solution(N,stages))
