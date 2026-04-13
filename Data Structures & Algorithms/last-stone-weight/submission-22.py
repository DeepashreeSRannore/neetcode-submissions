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

        #here we are performing 2 pop and 2 push every round so that becomes 3logn and we are doing it for n times so O(nlogn)
        #space complexity = O(n) - heap storage 





        