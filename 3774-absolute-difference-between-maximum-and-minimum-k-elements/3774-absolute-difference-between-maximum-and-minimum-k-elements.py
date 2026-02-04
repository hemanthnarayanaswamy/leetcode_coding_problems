class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxSum = sum(nums[-k:])
        minSum = sum(nums[:k])

        return maxSum - minSum