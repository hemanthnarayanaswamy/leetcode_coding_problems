class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        numSort = sorted(nums)

        if numSort[-1] >= numSort[-2]*2:
            return nums.index(numSort[-1])
        else:
            return -1