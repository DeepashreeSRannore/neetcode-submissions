class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return 
            if i>= len(nums) or total > target:
                return 
            
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res

        #time complexity = 2^(target)
        #space complexity = O(k*n) - where k is number of valid combination and n is the legth of those combination.
        