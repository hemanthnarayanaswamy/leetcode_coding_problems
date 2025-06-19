class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        # generate abs(x) for every x whose negation is also in s
        return max((abs(x) for x in s if -x in s), default=-1)
