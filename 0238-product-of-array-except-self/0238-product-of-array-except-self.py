class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n  # Step 1: Initialize result with 1s

        # Step 2: Compute prefix products (Left to Right)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]  # Update prefix for next iteration

        # Step 3: Compute postfix products (Right to Left)
        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix  # Multiply postfix value to result
            postfix *= nums[i]  # Update postfix for next iteration

        return result
        