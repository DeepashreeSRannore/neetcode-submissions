# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        def appendtoarray(root):
            if not root:
                return
            
            array.append(root.val)
            appendtoarray(root.left)
            appendtoarray(root.right)
           
        appendtoarray(root)
        array.sort()
        return array[k-1]

        
        
        