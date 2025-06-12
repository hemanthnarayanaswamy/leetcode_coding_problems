class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        flagFound = True 
        numsU = set(nums)

        while original in numsU:
                original *= 2
           
        return original