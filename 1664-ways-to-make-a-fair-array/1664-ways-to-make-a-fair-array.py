class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        post_odd = sum([nums[i] for i in range(n) if i % 2])
        post_even = total - post_odd
        preOdd = preEven = res = 0

        for i in range(n):
            num = nums[i]
            if i % 2:
                post_odd -= num
            else:
                post_even -= num

            if preOdd + post_even == preEven + post_odd:
                res += 1
            
            if i % 2:
                preOdd += num
            else:
                preEven += num
            
        return res