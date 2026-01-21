class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsTotal = sum(nums)

        if numsTotal < k:
            return numsTotal
        else:
            return numsTotal % k