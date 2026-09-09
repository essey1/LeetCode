# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            if root==None and subRoot!=None:
                return False
            if root!=None and subRoot==None:
                return False
            if root!=None and subRoot!=None:
                if root.val != subRoot.val:
                    return False
                else:
                    left = isSameTree(root.left, subRoot.left)
                    right = isSameTree(root.right, subRoot.right)
                    return left and right
        
        if isSameTree(root, subRoot):
            return True
        else:
            if root is None:
                return False
            return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)


       
            
            
        
        


        # if not root and not subRoot:
        #     return True
        
        # if root and subRoot:
        #     if root.val == subRoot.val:
        #         return True
        #     else:
        #         return False
        #     if root.val == subRoot.val:
        #         left = self.isSubtree(root.left, subRoot.left)
        #         right = self.isSubtree(root.right, subRoot.right)
        #         return left and right
        #     else:
        #         left = self.isSubtree(root.left, subRoot)
        #         right = self.isSubtree(root.right, subRoot)
        #         return left and right
        