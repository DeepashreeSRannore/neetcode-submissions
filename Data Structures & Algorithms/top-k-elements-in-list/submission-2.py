class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1
        countarray = []
        for n,count in hashmap.items():
            countarray.append([count,n])
        countarray.sort()
        result = []
        while len(result) < k:
            result.append(countarray.pop()[1])
        return result
            

        