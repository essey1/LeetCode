# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if node == None:
                return 0
            goodnode = 0
            if node.val >= maxval:
                maxval = node.val
                goodnode += 1
            left = dfs(node.left, maxval)
            right = dfs(node.right, maxval)
            return goodnode + left + right
        return dfs(root, root.val)

        