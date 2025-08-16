class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] == 1 and nums[-1] == n:
            return 0
        
        idx1, idxn = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                idx1 = i
            elif num == n:
                idxn = i
            
            if idx1 and idxn:
                break 
        
        if idx1 > idxn:
            count = (idx1 - 0) + (n-1 - idxn) - 1
        else:
            count = (idx1 - 0) + (n-1 - idxn)
        
        return count
