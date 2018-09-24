def FailureRate(N, stages):
    Tup = []
    for i in range(1, N + 1):
        cnt = 0
        lenStages = len(stages)
        for j in stages:
            if i == j:
                stages = stages[::-1]  # 오름차순, 너무 복잡하게 한듯....
                stages.remove(i)
                stages = stages[::-1]
                cnt += 1
            else:
                pass
        Tup.append((cnt / lenStages, -i))  # sort에서 idx도 오름차순으로 하기 위함 (i로 하면 내림차순)
    Tup = sorted(Tup, reverse=True)
    Output = []
    for i in Tup:
        Output.append(-i[1])
    return Output


if __name__ == '__main__':
    N = 5
    stages = [2, 1, 2, 6, 1, 2, 4, 3, 3]

    # N = 4
    # stages = [4,4,4,4,4]

    print(FailureRate(N, stages))
