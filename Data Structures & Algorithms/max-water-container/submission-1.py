class Solution:
    def maxArea(self, heights: List[int]) -> int:
        rp = len(heights)-1
        lp = 0
        area = 0
        lmax = 0
        rmax = 0
        dist = 0
        while(lp<rp):
            lmax = max(lmax, heights[lp])
            rmax = max(rmax, heights[rp])
            if lmax<rmax:
                
                dist = rp - lp
                area = max(area, dist * lmax)
                lp+=1

            else:
                
                dist = rp-lp
                area = max(area, dist * rmax)
                rp-=1


        return area
        