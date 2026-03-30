class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results =[]
        sum = 0
        if nums is None:
            return results
        nums.sort()
        for i,n in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue
            lp = i+1
            rp = len(nums)-1
            while lp<rp:
                sum = n+nums[lp]+nums[rp]
                if sum>0:
                    rp-=1
                elif sum<0:
                    lp+=1
                else:
                    results.append([n,nums[lp],nums[rp]])
                    lp+=1
                    while lp<rp and nums[lp]==nums[lp-1]:
                        lp+=1
        return results
            
        