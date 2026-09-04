class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefixMax = []
        numMax = 0
        numMin = float('inf')
        idx = -1

        for i in range(len(nums)):
            numMax = max(numMax, nums[i])
            prefixMax.append(numMax)

        for i in range(len(nums)-1, -1, -1):
            numMin = min(numMin, nums[i])
            if prefixMax[i] - numMin <= k:
                idx = i

        return idx