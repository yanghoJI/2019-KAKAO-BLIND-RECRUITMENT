# set input data
# algorithm complexity O(nlogn)
indata1 = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result1 = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

indata2 = [[6,10], [1,9], [3,8], [2,7], [4,7], [5,1], [8,9]]
result2 = [[1, 2, 3, 4, 5, 6, 7], [4, 6, 5, 3, 2, 7, 1]]

indata = indata2
result = result2

# make nodeList
nodeList = [indata[i] + [i+1] for i in range(len(indata))]
nodeList = sorted(nodeList, key=lambda x : x[1], reverse=True)


# make binary tree
class node:
    def __init__(self, info):
        self.number = info[2]
        self.data = info[:2]
        self.R = None
        self.L = None

def addnode(root, info):
    if info[0] > root.data[0]:
        if root.R == None:
            root.R = node(info)
        else:
            addnode(root.R, info)
    elif info[0] < root.data[0]:
        if root.L == None:
            root.L = node(info)
        else:
            addnode(root.L, info)
    else:
        raise ValueError('unexpected input')

root = node(nodeList[0])
for info in nodeList[1:]:
    addnode(root, info)


# do preorder, postorder and sol
def preorder(root, orderList):
    # priority root --> left --> right
    if root != None:
        orderList.append(root.number)
    if root.L != None:
        preorder(root.L, orderList)
    if root.R != None:
        preorder(root.R, orderList)

preorderList = []
preorder(root, preorderList)

def postorder(root, orderList):
    # priority left --> right --> root
    if root.L != None:
        postorder(root.L, orderList)
    if root.R != None:
        postorder(root.R, orderList)
    if root != None:
        orderList.append(root.number)

postorderList = []
postorder(root, postorderList)

sol = [preorderList, postorderList]
print('prediction : {}\nsolution : {}'.format(sol, result))
