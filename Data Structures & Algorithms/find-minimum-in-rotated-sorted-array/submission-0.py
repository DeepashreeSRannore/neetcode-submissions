class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums)-1
        min_ele = nums[0]

        while (lp<=rp):
            if nums[lp] <= nums[rp]:
                min_ele = min(min_ele,nums[lp])
                break
            mp = (lp+rp)//2
            min_ele = min(min_ele,nums[mp])
            if nums[lp] <= nums[mp]:
                lp = mp+1
            else:
                rp = mp -1

        return min_ele

            #TC = O(logn)
            #SC = O(1)
        