class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        idx1, idxn = nums.index(1), nums.index(n)
        count = idx1 + (n - 1 - idxn)

        return count - 1 if idx1 > idxn else count 