class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            result.append(abs(num*i - left_sum) + abs(num*n - right_sum))
            n -= 1
            left_sum += num
            right_sum -= num
        return result
        