class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        idx1, idxn = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                idx1 = i
            elif num == n:
                idxn = i
        
        count = (idx1 - 0) + (n-1 - idxn)

        return count - 1 if idx1 > idxn else count 
