class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 ={}
        hashmap2 = {}
        if len(s) != len(t):
            return False
        for n in s:
            hashmap1[n] = hashmap1.get(n,0)+1
        for m in t:
            hashmap2[m] = hashmap2.get(m,0)+1
        if hashmap1 != hashmap2:
            return False
        return True
        

        