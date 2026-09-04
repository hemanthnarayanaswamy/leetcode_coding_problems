class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        numMax = 0

        for i, num in enumerate(nums):
                numMax = max(numMax, num)
                numMin = min(nums[i:])

                if numMax - numMin <= k:
                    return i
        
        return -1
