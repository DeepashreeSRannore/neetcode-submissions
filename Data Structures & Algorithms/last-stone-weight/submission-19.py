class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)
        

        while len(maxheap) > 1:
            stone1 = -heapq.heappop(maxheap)
            stone2 = -heapq.heappop(maxheap)

            if stone1>stone2:
                val = stone1 - stone2
                heapq.heappush(maxheap, -val)

        return -maxheap[0] if maxheap else 0





        