class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        nums.sort()
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n] = True
        return False
        
 

        