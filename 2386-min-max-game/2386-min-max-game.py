class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            # pair up (nums[0],nums[1]), (nums[2],nums[3]), …
            pairs = zip(nums[::2], nums[1::2])
            # for each pair, take min if i is even, max if i is odd
            nums = [
                (a if a < b else b) if i % 2 == 0 else (a if a > b else b)
                for i, (a, b) in enumerate(pairs)
            ]
        return nums[0]
