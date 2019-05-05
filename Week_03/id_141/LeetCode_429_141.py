class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        parentQueue, childQueue = [root], list()
        res = list()
        while len(parentQueue) > 0:
            for p in parentQueue:
                for child in p.children:
                    childQueue.append(child)
            res.append([p.val for p in parentQueue])
            parentQueue = childQueue
            childQueue = list()
        return res

s1 = Solution()


n5 = Node(5, [])
n6 = Node(6, [])
n3 = Node(3, [n5, n6])

n2 = Node(2, [])
n4 = Node(4, [])
n1 = Node(1, [n3,n2, n4])
print(s1.levelOrder(n1))
