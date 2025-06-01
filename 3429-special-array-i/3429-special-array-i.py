class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if nums[i-1] % 2 == 0:
                    return False
            else:
                if nums[i-1] % 2 == 1:
                    return False
        
        return True
