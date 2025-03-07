class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)  # Array for lookup
        contains_1 = False

        # Mark the elements from nums in the lookup array
        for num in nums:
            if num == 1:
                contains_1 = True
            if 0 < num <= n:
                seen[num] = True
        
        if not contains_1: ## Some Edge cases 
            return 1

        # Iterate through integers 1 to n
        # return smallest missing positive integer
        for i in range(1, n + 1):
            if not seen[i]:
                return i

        # If seen contains all elements 1 to n
        # the smallest missing positive number is n + 1
        return n + 1