import timeit
# algorithm complexity O(nlogn)
# set input
indata1 = [3, 1, 2]
k1 = 5
result1 = 1

indata2 = [3, 1, 2]
k2 = 10
result2 = -1

indata3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k3 = 10
result3 = 2

indata4 = [1, 2, 3]
k4 = sum(indata4) - 1
result4 = 3

indata5 = list(range(1,200001))
k5 = sum(indata5) - 1
result5 = 200000

start = timeit.default_timer()
indata = indata5
k = k5
result = result5

# make and sort foodTimes
Foods = list(range(1,len(indata)+1))
foodTimes = zip(Foods, indata)
foodTimes = sorted(foodTimes, key= lambda x : x[1])
totalTime = sum(indata)

# make simulation function
def simul(indata, foodTimes, k):
    resTime = k
    loofNum = 0
    curlen = len(indata)
    poplist = set()
    for info in foodTimes:
        runtime = curlen * (info[1] - loofNum)
        if runtime <= resTime:
            resTime -= runtime
            poplist.add(info[0])
            curlen -= 1
            loofNum += info[1] - loofNum
        else:
            solIndex = resTime % curlen
            break
    return (solIndex, poplist)

# sol
if k >= totalTime:
    sol = -1
else:
    solIndex, poplist = simul(indata, foodTimes, k)
    resFoods = []
    for food in Foods:
        if food in poplist:
            pass
        else:
            resFoods.append(food)
    sol = resFoods[solIndex]
end = timeit.default_timer()
print('prediction : {}\t\tsolution : {}\t\trun time {:.6f} sec'.format(sol, result, end - start))