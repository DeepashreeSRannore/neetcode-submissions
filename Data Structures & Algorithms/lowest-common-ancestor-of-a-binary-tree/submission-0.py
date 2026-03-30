# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #If root is present then proceed with the processing
        #first check if the root is equal to either p or q if yes return root
        #if no, then recursive serch in both right and left subtree and get the result
        #if p and q are found then return its root
        #if p or q is the root itself return that
        while root:
            if root == p or root == q:
                return root
            
            left = self.lowestCommonAncestor(root.left,p,q)
            right = self.lowestCommonAncestor(root.right,p,q)

            if left and right:
                return root
            
            return left if left else right

#Time complexity = O(n) - worst case scenario it can only traverse or visit all the nodes present in the tree which is n
#Space complexity = 0(h) - worst case scenario the left and right subtree can hold respective nodes of height h
        