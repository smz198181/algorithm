# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return 1 + self.maxDepth(root.right)
        elif root.left != None and root.right == None:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

node4 = TreeNode(15)
node5 = TreeNode(7)

node3 = TreeNode(20)
node3.left = node4
node3.right = node5

node2 = TreeNode(9)
node1 = TreeNode(3)
node1.left = node2
node1.right = node3

s1 = Solution()
print(s1.maxDepth(node1))


