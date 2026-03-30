class Solution:
    def climbStairs(self, n: int) -> int:
        current_value = previous_value = 1
        for i in range(n-1):
            temp = current_value
            current_value += previous_value
            previous_value = temp
        return current_value