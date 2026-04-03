class Solution:
    def trap(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        sum = 0 
        lmax = 0
        rmax = 0
        while(lp<rp):
            lmax=max(height[lp],lmax)
            rmax=max(height[rp],rmax)
            if lmax<rmax:
                sum+=lmax-height[lp]
                lp+=1
            else:
                sum+=rmax-height[rp]
                rp-=1
        return sum

        #2 pointer approach
        #TC=O(n)
        #SC=0(1)
