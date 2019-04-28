# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root) :
        nodeArr = []
        self.TraverseBinary(root, nodeArr)
        nodeArr.sort()
        if nodeArr[-1] == nodeArr[0]:
            return -1
        for num in nodeArr:
            if num == nodeArr[0]:
                continue
            else:
                return num
            
        
    def TraverseBinary(self, root, nodeArr):
        
        if root == None:
            return
        if root.left != None:
            self.TraverseBinary(root.left, nodeArr)
        nodeArr.append(root.val)
        if root.right != None:
            self.TraverseBinary(root.right, nodeArr)
