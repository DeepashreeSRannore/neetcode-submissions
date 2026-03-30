class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap ={}
        temparray =[]
        finalarray=[]
        #runs for n 
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
        #runs for u in worst case n
        for key,value in hashmap.items():
            temparray.append([value,key])
            #runs for nlogn time
        temparray.sort(reverse=False)
        #runs for k time
        while len(finalarray)<k:
            finalarray.append(temparray.pop()[1])
        return finalarray
#time complexity = O(n+nlogn+k) = O(nlogn)
#space complexity = o(2n)
