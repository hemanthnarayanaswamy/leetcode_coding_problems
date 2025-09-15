class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ct = 0
        numPrevZero = 0
        for num in nums:
            if num == 0:
                numPrevZero += 1
            else:
                if numPrevZero:
                    ct += numPrevZero * (numPrevZero + 1) // 2
                numPrevZero = 0
        if numPrevZero:
            ct += numPrevZero * (numPrevZero + 1) // 2
        return ct