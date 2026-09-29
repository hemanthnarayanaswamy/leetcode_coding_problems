class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        post_odd = sum([nums[i] for i in range(n) if i % 2])
        post_even = total - post_odd
        preOdd = preEven = res = 0

        for i in range(n):
            if i % 2:
                post_odd -= nums[i]
            else:
                post_even -= nums[i]

            if preOdd + post_even == preEven + post_odd:
                res += 1
            
            if i % 2:
                preOdd += nums[i]
            else:
                preEven += nums[i]
            
        return res