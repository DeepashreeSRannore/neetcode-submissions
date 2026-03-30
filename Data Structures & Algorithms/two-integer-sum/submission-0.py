class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        for i,n in enumerate(nums):
            required_num = target - n
            if required_num in hashmap:
                return [hashmap[required_num], i]
            hashmap[n] = i   
        return