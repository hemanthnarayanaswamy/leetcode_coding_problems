class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_prefix = []
        right_prefix = []
        left_sum = 0
        numsSum = sum(nums)
        res = 0

        for i in range(len(nums)):
            l = left_sum + nums[i]
            r = abs(numsSum - left_sum)
            left_prefix.append(l)
            right_prefix.append(r)
            left_sum = l

            if nums[i] == 0:
                if left_prefix[i] == right_prefix[i]:
                    res += 2
                elif abs(left_prefix[i] - right_prefix[i]) == 1:
                    res += 1

        return res
