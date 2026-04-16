class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finaldict = defaultdict(list)
        for string in strs:
            countarray = [0] * 26
            for char in string:
                countarray[ord(char) - ord("a")] +=1
            finaldict[tuple(countarray)].append(string)
        return list(finaldict.values())
        