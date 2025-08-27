class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        minPrefix = min(prefixSum)

        if minPrefix < 0:
            return 1 + abs(minPrefix)
        else:
            return 1