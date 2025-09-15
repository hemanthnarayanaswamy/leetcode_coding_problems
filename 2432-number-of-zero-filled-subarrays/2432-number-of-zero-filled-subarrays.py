class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        zeroCount = 0

        for num in nums:
            if num != 0:
                if zeroCount:
                    res += ((zeroCount) * (zeroCount + 1)) // 2
                    zeroCount = 0
            else:
                zeroCount += 1
        
        res += ((zeroCount) * (zeroCount + 1)) // 2
        
        return res
        