class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={0:0}
      #  coins.sort()
        def min_coin(amt):
            if amt in memo:
                return memo[amt]
            minn = float('inf')
            for coin in coins:
                difference = amt - coin
                if difference < 0:
                    break
                minn = min(minn, 1+ min_coin(difference))
            memo[amt] = minn
            return memo[amt]

        result = min_coin(amount)
        if result < float('inf'):
            return result
        else: 
            return -1
        