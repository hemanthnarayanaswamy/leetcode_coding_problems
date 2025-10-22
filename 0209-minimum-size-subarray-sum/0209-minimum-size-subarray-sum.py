class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        best = float('inf')
        for right, x in enumerate(nums):
            curr += x
            while curr >= target:
                best = min(best, right - left + 1)
                curr -= nums[left]
                left += 1
        return 0 if best == float('inf') else best
