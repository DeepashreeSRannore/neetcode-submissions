# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpointer = head
        fastpointer = head

        while fastpointer and fastpointer.next:
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next

            if slowpointer == fastpointer:
                return True

        return False
        
        #Time complexity = is approximately O(n) since it runs on loops
        #Space complexity = O(1)