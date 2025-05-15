class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        if n%2 == 1:
            median = nums[(n - 1) // 2]
        else:
            i = n // 2
            median = (nums[i] + nums[i-1]) // 2

        return sum([abs(num - median) for num in nums])