class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            req=target-n
            if req in hashmap:
                return [hashmap[req],i]
            hashmap[n]=i
        