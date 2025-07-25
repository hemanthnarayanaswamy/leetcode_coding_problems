class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniqNum = set()
        maxNum = max(nums)
        if max(nums) > 0:
            for num in nums:
                if num > 0 and num not in uniqNum:
                    uniqNum.add(num)
        else:
            return maxNum

        return sum(uniqNum)