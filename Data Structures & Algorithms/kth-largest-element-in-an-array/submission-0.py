class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-s for s in nums]
        heapq.heapify(maxheap)
        max_element = None

        for i in range(k):
            max_element = -heapq.heappop(maxheap)
        return max_element







        