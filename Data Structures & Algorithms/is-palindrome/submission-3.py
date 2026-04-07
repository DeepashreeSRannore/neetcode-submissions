class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = " ".join(a for a in s if a.isalnum())
        lp = 0
        rp = len(new_str)-1
        
        
        while lp < rp:
            if new_str[lp].lower() != new_str[rp].lower():
                return False
            lp+=1
            rp-=1
        
        else:
            return True
        

        