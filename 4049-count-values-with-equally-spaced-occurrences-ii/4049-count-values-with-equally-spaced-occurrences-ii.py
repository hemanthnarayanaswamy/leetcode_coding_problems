class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        numsOccurrences = defaultdict(list)

        for i, num in enumerate(nums):
            numsOccurrences[num].append(i)
        
        res = 0

        for val in numsOccurrences.values():
            n1 = len(val)
            if n1 < 3:
                continue 
            idxDiff = set()
            for i in range(n1-1):
                idxDiff.add(val[i+1]-val[i])
            
            if len(idxDiff) == 1:
                res += 1
        
        return res