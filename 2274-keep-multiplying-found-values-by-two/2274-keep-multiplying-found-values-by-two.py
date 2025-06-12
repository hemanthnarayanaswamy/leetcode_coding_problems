class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        flagFound = True 
        numsU = set(nums)

        while flagFound:
            if original in numsU:
                original *= 2
            else:
                return original
