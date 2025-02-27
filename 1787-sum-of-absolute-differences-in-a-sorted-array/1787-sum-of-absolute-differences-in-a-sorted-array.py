class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = [0] * n
        
        for i in range(len(nums)):
            right_sum -= nums[i]
            result[i] = (nums[i]*i - left_sum) + (right_sum - nums[i] * (n-i-1))
            left_sum += nums[i]
            
        return result
        