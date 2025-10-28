class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_sum = 0
        numsSum = sum(nums)
        res = 0

        for num in nums:
            l = left_sum + num
            r = abs(numsSum - left_sum)
            left_sum = l

            if num == 0:
                diff = abs(l - r)
                if diff == 0:
                    res += 2
                elif diff == 1:
                    res += 1

        return res
