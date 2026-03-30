class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        results=[]
        final = []
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1
        for key,value in hashmap.items():
            results.append([value,key])
        results.sort(reverse=False)
        while len(final) < k:
            final.append(results.pop()[1])
        return final
        