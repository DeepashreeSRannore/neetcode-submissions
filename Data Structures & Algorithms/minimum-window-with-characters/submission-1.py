class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        l = 0
        countT = {}
        windows = {}
        for c in t:
            countT[c] = countT.get(c,0)+1
        
        have = 0
        need = len(countT)
        res = [-1,-1]
        reslen = float("infinity")

        for r in range(len(s)):
            windows[s[r]] = windows.get(s[r],0)+1
            c=s[r]
        
            if c in countT and windows[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r-l+1)<reslen:
                    reslen = (r-l+1)
                    res = [l,r]
                
                windows[s[l]] -= 1
                if s[l] in countT and windows[s[l]]<countT[s[l]]:
                    have -=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen != float('infinity') else ''
#Time complexity = O(n)
#Space complexity = O(1)




        