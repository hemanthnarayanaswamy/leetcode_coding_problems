class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1

        while i > 0 and nums[i] > nums[i-1]:
            i -= 1
        
        return i
        