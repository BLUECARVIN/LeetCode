# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def walk(node):
            left = 0
            right = 0
            if node.left != None:
                left = walk(node.left)
            if node.right != None:
                right = walk(node.right)
            return 1 + max(left, right)
        if root:
            return walk(root)
        else:
            return 0