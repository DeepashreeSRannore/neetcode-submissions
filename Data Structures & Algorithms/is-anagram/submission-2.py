class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap ={}
        hashmap2 ={}
        for c in s:
            hashmap[c] = hashmap.get(c,0)+1
        for ch in t:
            hashmap2[ch] = hashmap2.get(ch,0)+1
        if hashmap == hashmap2:
            return True
        return False

        
        
        