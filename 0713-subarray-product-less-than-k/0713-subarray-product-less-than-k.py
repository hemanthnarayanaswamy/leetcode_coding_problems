class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prod = 1
        left = 0
        res = 0

        if k <= 1:
            return res

        for right, num in enumerate(nums):
            prod *= num

            while prod >= k:
                prod //= nums[left]
                left += 1

            res += (right - left + 1)
        
        return res
    