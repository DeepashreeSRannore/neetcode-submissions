class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap =[]
        
        for x,y in points:
            dis = self.distance(x,y)
            if len(maxheap) < k:
                
                heapq.heappush(maxheap,(-dis,x,y))
            else:
                heapq.heappush(maxheap,(-dis,x,y))
                heapq.heappop(maxheap)
        return [(x,y) for d,x,y in maxheap]   
              




    def distance(self,x,y):
        dis = ((x)**2 + (y)**2)
        return dis

        