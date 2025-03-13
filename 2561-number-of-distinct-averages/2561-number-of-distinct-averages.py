class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        result = set()
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            result.add((nums[l]+nums[r])/2)
            l += 1
            r -= 1
        return len(result)
        