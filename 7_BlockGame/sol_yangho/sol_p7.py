# show board
def showboard(board):
    b = '#' * len(board[0])
    print(b)
    for r in board:
        print(*r)
    print(b)

# set input
indata1 = [[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,4,0,0,0],
[0,0,0,0,0,4,4,0,0,0],
[0,0,0,0,3,0,4,0,0,0],
[0,0,0,2,3,0,0,0,5,5],
[1,2,2,2,3,3,0,0,0,5],
[1,1,1,0,0,0,0,0,0,5]]
result1 = 2

indata2 = [[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,4,0,0,0],
[0,0,0,0,0,4,4,0,0,0],
[0,0,0,2,3,0,4,0,0,0],
[0,2,2,2,3,0,0,0,5,5],
[1,0,0,0,3,3,0,0,0,5],
[1,1,1,0,0,0,0,0,0,5]]
result2 = 2

indata3 = [[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,4,0,0,0],
[0,0,0,0,0,4,4,4,0,0],
[0,0,0,2,3,0,0,0,0,0],
[0,2,2,2,3,0,0,0,5,5],
[1,0,0,0,3,3,6,0,0,5],
[1,1,1,0,0,6,6,6,0,5]]
result3 = 5

indata4 = [[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[7,7,7,0,0,0,4,0,0,0],
[0,7,0,0,0,4,4,4,0,0],
[0,0,0,2,3,0,0,0,0,0],
[0,2,2,2,3,0,0,0,5,5],
[1,0,0,0,3,3,6,0,0,5],
[1,1,1,0,0,6,6,6,0,5]]
result4 = 3

indata5 = [[0,0,0,0,0,0,0,0,0,0],
[0,4,0,0,0,0,0,0,0,0],
[0,4,4,4,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,3,3,3,0,0,0,0],
[0,0,0,0,3,0,0,0,0,0],
[0,0,0,2,0,6,0,0,5,5],
[1,2,2,2,0,6,6,6,0,5],
[1,1,1,0,0,0,0,0,0,5]]
result5 = 4

indata = indata1
result = result1
showboard(indata)


# define board size
rowNum = len(indata)
colNum = len(indata[0])


# define block class
class Block:
    def __init__(self, blockNumber):
        self.blockNumber = blockNumber
        self.rmBlock = set()
        self.block = set()
        self.offset = [51, 51]
        self.removable = False

    def addcoodi(self, coordi):
        if coordi[0] < self.offset[0]:
            self.offset[0] = coordi[0]
        if coordi[1] < self.offset[1]:
            self.offset[1] = coordi[1]
        self.block.add(coordi)

    def getinfo(self):
        # remove offset
        cleanBlock = set([(coordi[0] - self.offset[0], coordi[1] - self.offset[1]) for coordi in self.block])

        # define Removable block coordi set
        b1 = set([(0,0), (1,0), (1,1), (1,2)])
        rm1 = set([(0,1), (0,2)])
        b2 = set([(2,0), (2,1), (1,1), (0,1)])
        rm2 = set([(0, 0), (1, 0)])
        b3 = set([(0, 0), (1, 0), (2, 0), (2, 1)])
        rm3 = set([(0, 1), (1, 1)])
        b4 = set([(1, 0), (1, 1), (1, 2), (0, 2)])
        rm4 = set([(0, 0), (0, 1)])
        b5 = set([(1, 0), (1, 1), (1, 2), (0, 1)])
        rm5 = set([(0, 0), (0, 2)])
        rmBlist = [b1, b2, b3, b4, b5]
        rm = [rm1, rm2, rm3, rm4, rm5]

        # get block info
        for i, b in enumerate(rmBlist):
            if cleanBlock == b:
                self.removable = True
                self.rmBlock = set([(coordi[0] + self.offset[0], coordi[1] + self.offset[1]) for coordi in rm[i]])
                break


# generate block class
poList = [rowNum] * colNum
blockDict = {}
for row in range(rowNum):
    for col in range(colNum):
        v = indata[row][col]
        if v != 0:
            if v in blockDict:
                blockDict[v].addcoodi((row, col))
            else:
                blockDict[v] = Block(v)
                blockDict[v].addcoodi((row, col))

            if row < poList[col]:
                poList[col] = row
for b in blockDict:
    blockDict[b].getinfo()

# sol
rmCount = 0
for row in range(rowNum):
    for col in range(colNum):
        v = indata[row][col]
        if v != 0:
            targetB = blockDict[v]
            if targetB.removable:
                flag = True
                for coor in targetB.rmBlock:
                    if coor[0] >= poList[coor[1]]:
                        flag = False
                        break
                if flag == True:
                    rmCount += 1
                    blockDict.pop(v)
                    for coor in targetB.block:
                        indata[coor[0]][coor[1]] = 0
                        if coor[0] <= poList[coor[1]]:
                            temp = coor[0] + 1
                            for i in range(temp, rowNum):
                                if indata[i][coor[1]] == 0:
                                    temp += 1
                                else:
                                    break
                            poList[coor[1]] = temp
                    #print(poList)

showboard(indata)
print('prediction : {}\t\tsolution : {}'.format(rmCount, result))