class Solution:
    def secondHighest(self, s: str) -> int:
        alphabates = 'abcdefghijklmnopqrstuvwxyz'

        nums = set(int(char) for char in s if char not in alphabates)
        nums = sorted(nums, reverse=True)

        if len(nums) > 1:
            return nums[1]
        else:
            return -1