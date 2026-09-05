class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefixMax = [0]
        numMin = float('inf')
        idx = -1

        for num in nums:
            prefixMax.append(max(prefixMax[-1], num))

        for i in range(n-1, -1, -1):
            numMin = min(numMin, nums[i])
            if prefixMax[i+1] - numMin <= k:
                idx = i

        return idx