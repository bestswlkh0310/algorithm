import sys

sys.setrecursionlimit(10**5)

arr = []

while True:
    try:
        arr.append(int(input()))
    except:
        break


class Node:
    def __init__(self, key, left=None, right=None):
        self.key=key
        self.left=left
        self.right=right


root = Node(arr[0])
del arr[0]

def insert(i, node):
    newNode = Node(i)
    if node.key > i:
        if node.left == None:
            node.left = newNode
        else:
            insert(i, node.left)
    else:
        if node.right == None:
            node.right = newNode
        else:
            insert(i, node.right)

# O(nLogn)
for i in arr:
    insert(i, root)
# O(n)
def search(node):
    if node.left != None: search(node.left)
    if node.right != None: search(node.right)
    print(node.key)

search(root)
