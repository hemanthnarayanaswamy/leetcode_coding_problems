class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        numsOccurrences = defaultdict(list)

        for i, num in enumerate(nums):
            numsOccurrences[num].append(i)
        
        res = 0

        for v in numsOccurrences.values():
            if len(v) != 3:
                continue 
            
            i1, i2, i3 = v
            if i2 - i1 == i3 - i2:
                res += 1
        
        return res