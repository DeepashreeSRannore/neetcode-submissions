class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        lp = 0 
        longstr=0

        for rp in range(len(s)):
            while s[rp] in sets:
                sets.remove(s[lp])
                lp+=1
            sets.add(s[rp])
            strlen = rp - lp + 1
            longstr = max(longstr, strlen)
        return longstr
        #Tc = O(n)
        #Sc = O(n)
        