class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        checkPoint = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                checkPoint = i
        
        return checkPoint