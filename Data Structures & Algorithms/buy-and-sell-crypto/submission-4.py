class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lp = 0
        rp = 1
        while rp<len(prices):
            if prices[lp]>=prices[rp]:
                lp=rp
                rp+=1
            else:
                profit = prices[rp]-prices[lp]
                max_profit = max(max_profit,profit)
                rp+=1
        return max_profit


            #time complexity = O(n)
            #space complexity = O(1)
            
            

        