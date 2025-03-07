class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_unique = set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums_unique:
                return i 
        return len(nums) + 1
        