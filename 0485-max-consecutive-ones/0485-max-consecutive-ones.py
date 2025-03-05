class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum, max_sum = 1, 1 
        for num in nums:
            if sum*num:
                sum += num 
            else:
                sum = 1
            max_sum = max(sum, max_sum)
        return max_sum - 1

        