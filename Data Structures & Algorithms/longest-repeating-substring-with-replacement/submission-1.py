class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        lp = 0
        max_len = 0 

        for rp in range(len(s)):
            count[s[rp]] = 1 + count.get(s[rp], 0)
            while (rp-lp+1)- max(count.values()) > k :
                count[s[lp]] -= 1
                lp += 1
            max_len = max(max_len, (rp-lp+1))
        return max_len

#Time complexity = O(26.n)
#Space complexity = O(1)
        