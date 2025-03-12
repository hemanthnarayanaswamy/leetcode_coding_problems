class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float('-inf')
        n = len(nums)
        if n <= k:
            result = sum(nums) / k
        else:
            initial_sum = sum(nums[0:k])
            result = initial_sum / k
        
        for i in range(1, n):
            if i+k-1 < n:
                initial_sum = initial_sum - nums[i-1] + nums[i+k-1]
                result = max(initial_sum / k, result)
        return result

        