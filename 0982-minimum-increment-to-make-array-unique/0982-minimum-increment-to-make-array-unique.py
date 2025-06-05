class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        operations = 0
        nums = sorted(nums)

        for i in range(1,len(nums)):
            pre,cur = nums[i-1], nums[i]

            if cur <= pre:
                nums[i] = pre + 1
                operations += pre - cur + 1
        
        return operations
