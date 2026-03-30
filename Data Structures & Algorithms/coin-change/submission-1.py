class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        memo = {0:0}
        def min_coins(amt):
            if amt in memo:
                return memo[amt]
            minimum = float('inf')
            for coin in coins:
                difference = amt - coin
                if difference < 0:
                    continue
                minimum = min(minimum, 1 + min_coins(difference))
            memo[amt] = minimum
            return minimum
        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1

        