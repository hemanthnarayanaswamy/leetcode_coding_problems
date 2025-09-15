class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroCount = res = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else: 
                if zeroCount:
                    res += ((zeroCount) * (zeroCount + 1)) // 2
                    zeroCount = 0

        if zeroCount:
            res += ((zeroCount) * (zeroCount + 1)) // 2
        
        return res