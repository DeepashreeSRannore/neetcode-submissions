class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x,y in points:
            val = self.distance(x,y)
            if len(max_heap)<k:           
                heapq.heappush(max_heap,(-val,x,y))
            else:
                heapq.heappush(max_heap,(-val,x,y))
                heapq.heappop(max_heap)
        return [(x,y) for d,x,y in max_heap]

    def distance(self,x,y):
        d = x**2 + y**2
        return d
        