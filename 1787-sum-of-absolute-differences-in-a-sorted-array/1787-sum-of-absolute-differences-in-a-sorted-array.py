class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = [0] * n
        for i in range(len(nums)):
            result[i] = abs(nums[i]*i - left_sum) + abs(nums[i]*n - right_sum)
            n -= 1
            left_sum += nums[i]
            right_sum -= nums[i]
        return result
        