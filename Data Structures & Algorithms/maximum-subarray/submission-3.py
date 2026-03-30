class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            if len(nums) == 1:
                return n
            current_sum = max(n, current_sum + n)
            maxsum = max(maxsum, current_sum)
        return maxsum
        
        