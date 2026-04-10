class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        max = 1000

        for i in range(1, max):
            n = i * k
            if n not in nums:
                return n