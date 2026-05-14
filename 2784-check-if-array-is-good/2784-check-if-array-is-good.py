class Solution:
    def isGood(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 2:
            return False

        nums.sort()
        
        for i in range(length-1):
            if nums[i] != i+1:
                return False
        
        if nums[length-1] == nums[length-2]:
            return True
        else:
            return False