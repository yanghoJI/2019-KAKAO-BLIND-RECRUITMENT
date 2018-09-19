# set input data
N1 = 5
input1 = [2, 1, 2, 6, 2, 4, 3, 3]
sol1 = [3,4,2,1,5]
N2 = 4
input2 = [4,4,4,4,4]
sol2 = [4,1,2,3]
N = N1
input = input1
sol = sol1

# conunt sort
Clist = [0] * (N + 1)
for v in input:
    Clist[v - 1] += 1

# calculate Clist
zerolist = []
orderlist = []
cntsum = 0
if Clist[-1] != 0:
    cntsum += Clist[-1]
for index in range(N - 1, -1, -1):
    if Clist[index] == 0:
        zerolist.append(index + 1)
    else:
        orderlist.append([index + 1, Clist[index] / (cntsum + Clist[index])])
        cntsum += Clist[index]

# sort orderlist
orderlist = reversed(orderlist)
zerolist = reversed(zerolist)
orderlist = sorted(orderlist, key= lambda x : x[1], reverse=True)

# merge list
solution = [x[0] for x in orderlist] + list(zerolist)
print('prediction : {}\nsol : {}'.format(solution, sol))
