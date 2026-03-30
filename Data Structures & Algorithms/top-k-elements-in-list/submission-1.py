class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        outputlist = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0)+1
        for m, count in hashmap.items():
            outputlist.append([count,m])
        outputlist.sort()
        result = []
        while len(result) < k:
            result.append(outputlist.pop()[1])


        return result
            

        