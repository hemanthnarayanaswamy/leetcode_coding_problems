class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            current_num = nums[i]
            right_sum -= current_num
            result[i] = (current_num*i - left_sum) + (right_sum - current_num * (n-i-1))
            left_sum += current_num
            
        return result
        