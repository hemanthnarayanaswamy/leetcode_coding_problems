class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > first:
                first, second, third = num , first, second
            elif num > second and num < first: ## first > num > second
                second, third = num, second 
            elif num > third and num < second: ## second > num > third
                third = num 
        
        if third != float('-inf'):
            return third
        else:
            return first