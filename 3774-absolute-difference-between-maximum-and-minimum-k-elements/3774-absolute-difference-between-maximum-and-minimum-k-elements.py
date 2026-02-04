class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        largeSum = sum(nums[-k:])
        smallSum = sum(nums[:k])

        return largeSum - smallSum