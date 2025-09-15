class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = []
        zeroCount = 0

        for num in nums:
            if num != 0:
                if zeroCount:
                    res.append(zeroCount)
                    zeroCount = 0
            else:
                zeroCount += 1
        
        if zeroCount: 
            res.append(zeroCount)
        
        return sum((n*(n+1))//2 for n in res)
        