# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(leftboundary,root,rightboundary):
            if not root:
                return True
            if not (root.val>leftboundary and root.val<rightboundary):
                return False
            return (valid(leftboundary,root.left,root.val) and valid(root.val,root.right,rightboundary))

        return (valid(float('-inf'),root,float('inf')))

        #time complexity = O(2n) = O(n)
        #space complexity = O(1)
        