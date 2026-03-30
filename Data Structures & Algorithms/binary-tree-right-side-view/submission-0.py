# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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

            results.append(temparray[::-1][0])
        return results
        