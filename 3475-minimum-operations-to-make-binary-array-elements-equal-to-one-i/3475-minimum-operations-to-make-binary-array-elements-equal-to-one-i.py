class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1
        
        if nums[i+1] == 0 or nums[i+2] == 0:
            return -1
        
        return count
