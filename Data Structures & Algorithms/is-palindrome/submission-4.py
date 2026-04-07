class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join(a for a in s if a.isalnum())
        lp = 0
        rp = len(s)-1
        
        
        while lp < rp:
            if s[lp].lower() != s[rp].lower():
                return False
            lp+=1
            rp-=1
        
        else:
            return True

        #TC=O(n)
        #SC=O(n)
        

        