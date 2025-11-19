class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numsU = set(nums)

        while original in numsU:
                original *= 2
           
        return original