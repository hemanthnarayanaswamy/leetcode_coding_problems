class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum, digit_sum = 0, 0

        for num in nums:
            element_sum += num 
            while num:
                digit_sum += num % 10 
                num = num // 10
                
        return abs(element_sum - digit_sum)