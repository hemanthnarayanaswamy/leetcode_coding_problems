class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsTotal = sum(nums)

        return numsTotal % k