class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefixMin = [0] * n
        prefixMin[-1] = nums[-1]
        numMax = 0

        for i in range(n-2, -1, -1):
            prefixMin[i] = min(nums[i], prefixMin[i+1])


        for i, num in enumerate(nums):
                numMax = max(numMax, num)
                numMin = prefixMin[i]

                if numMax - numMin <= k:
                    return i
        
        return -1
