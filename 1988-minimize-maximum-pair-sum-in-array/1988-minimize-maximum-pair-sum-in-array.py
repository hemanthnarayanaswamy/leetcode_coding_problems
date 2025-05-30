class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        left, right = 0, n-1
        result = 0

        while left < right:
            result = max(result, nums[left]+nums[right])
            left += 1
            right -= 1
            
        return result