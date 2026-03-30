
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for str in strs:
            count = [0]*26 #number of lower case letters = 26 (a-z)
            for character in str:
                count[ord(character) - ord("a")] += 1
            hashmap[tuple(count)].append(str)
        return list(hashmap.values())
        

