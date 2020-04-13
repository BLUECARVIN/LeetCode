# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def mirrorNode(node):
            if node:
                p = node.left
                node.left = node.right
                node.right = p
                mirrorNode(node.left)
                mirrorNode(node.right)
                return node
            else:
                pass
        return mirrorNode(root)