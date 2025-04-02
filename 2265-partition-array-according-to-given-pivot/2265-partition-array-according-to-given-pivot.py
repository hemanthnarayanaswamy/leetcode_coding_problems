class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n # List to store the Result 
        left = 0 
        right = n - 1 

        for i, j in zip(range(n), range(n-1,-1,-1)): # We do a Iteration while combining both forward and Reverse Iterations
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1 
        
        while left <= right:
            result[left] = pivot
            left += 1
        
        return result