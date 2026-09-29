class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        post_even = sum(nums[::2])
        post_odd = sum(nums[1::2])
        pre_odd = pre_even = res = 0

        for i in range(n):
            num = nums[i]
            if i % 2:
                post_odd -= num
                if pre_odd + post_even == pre_even + post_odd:
                    res += 1
                pre_odd += num
            else:
                post_even -= num
                if pre_odd + post_even == pre_even + post_odd:
                    res += 1
                pre_even += num
            
        return res