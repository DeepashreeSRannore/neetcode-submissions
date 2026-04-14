# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
            else:
                return
        dfs(root)
        return res
#inorder = left -> root -> right
#preorder = root -> left -> right
#postorder = left -> right -> root
        
        