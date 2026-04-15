# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while current:
            #if current value is greater than both left and right value then move to the right subtree
            if current.val < q.val and current.val < p.val:
                current = current.right
            #if current value is lesser than both left and right value then move to the left subtree
            elif current.val > q.val and current.val > p.val:
                current = current.left
            # this covers 3 conditions: when p and q falls on different directions, when p is the ancestor node of itself , when q is the ancestor node of itself
            else:
                return current

#time complexity : 0(logn)
#space complexity : 0(1)

        