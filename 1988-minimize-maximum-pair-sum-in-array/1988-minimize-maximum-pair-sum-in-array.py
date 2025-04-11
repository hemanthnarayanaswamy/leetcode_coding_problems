class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        nums.sort()
        result = 0

        while left < right:
            result = max(result, nums[left]+nums[right])
            left += 1
            right -= 1
            
        
        return result

        