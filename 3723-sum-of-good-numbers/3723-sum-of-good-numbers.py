class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            p = i - k
            n = i + k

            if p > -1 and n < len(nums):
                if nums[i] > nums[p] and nums[i] > nums[n]:
                    res += nums[i]
            elif p < 0 and n < len(nums):
                if nums[i] > nums[n]:
                    res += nums[i]
            elif p > -1 and n >= len(nums):
                if nums[i] > nums[p]:
                    res += nums[i]
            else:
                res += nums[i]

        return res   
