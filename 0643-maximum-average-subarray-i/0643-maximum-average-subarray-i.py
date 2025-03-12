class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float('-inf')
        if len(nums) <= k:
            result = sum(nums) / k
        else:
            initial_sum = sum(nums[0:k])
            result = initial_sum / k
        
        for i in range(1, len(nums)):
            if i+k-1 < len(nums):
                initial_sum = initial_sum - nums[i-1] + nums[i+k-1]
                temp_avg = initial_sum / k
                if temp_avg > result:
                    result =  temp_avg
        return result

        