class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum, max_sum = 0, 0
        for num in nums:
            if num == 1:
                sum += 1 
            else:
                sum = 0
            max_sum = max(sum, max_sum)
        return max_sum 

        