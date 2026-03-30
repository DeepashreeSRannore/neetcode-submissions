class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lp, rp = 0,len(nums)-1

        while lp <= rp:
            mp = (lp+rp)//2
            if nums[mp] == target or nums[lp] == target or nums[rp] == target:
                return True
            if nums[mp] == nums[lp] == nums[rp]:
                lp += 1
                rp -= 1
            #left portion
            elif nums[lp] <= nums[mp]:
                if target > nums[mp] or target < nums[lp]:
                    lp = mp + 1
                else:
                    rp = mp -1
            
            #right portion
            else:
                if target < nums[mp] or target > nums[rp]:
                    rp = mp -1 
                else: 
                    lp = mp + 1
        return False

        #time complexity = 0(logn)
        #space complexity = 0(1)
        