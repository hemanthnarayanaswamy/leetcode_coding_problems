class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        left_min = [0] * n
        left_min[0] = nums[0]

        for i in range(1, n):
            left_min[i] = min(nums[i], left_min[i-1])
        
        right_min = [0] * n
        right_min[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            right_min[i] = min(nums[i], right_min[i+1])
        
        res = float('inf')

        for i in range(1, n-1):
            left = left_min[i-1]
            right = right_min[i+1]
            current = nums[i]

            if current > left and current > right:
                res = min(res, left + current + right)
                
        return -1 if res == float('inf') else res
