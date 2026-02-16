class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        checkPoint = 0
        n = len(nums)
        prev = nums[0]

        for i in range(1, n):
            curr = nums[i]
            if curr <= prev:
                checkPoint = i
            prev = curr
        
        return checkPoint