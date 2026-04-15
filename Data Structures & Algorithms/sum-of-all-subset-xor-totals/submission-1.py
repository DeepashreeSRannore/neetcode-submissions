class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(x,total):
            if x==len(nums):
                return total
            return dfs(x+1,total ^ nums[x]) + dfs(x+1,total)

        return dfs(0,0)

        #time complexity = O(2^n)
        #space complexity = O(1)
        