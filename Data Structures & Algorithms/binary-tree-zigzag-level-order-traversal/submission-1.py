# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        if root is None:
            return results
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            temparray = []

            for i in range(n):
                node = queue.popleft()
                temparray.append(node.val)
            
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if len(results)%2 == 1:
                temparray = temparray[::-1]
            results.append(temparray)
        return results

        #TC = O(n)
        #SC = O(n)
        