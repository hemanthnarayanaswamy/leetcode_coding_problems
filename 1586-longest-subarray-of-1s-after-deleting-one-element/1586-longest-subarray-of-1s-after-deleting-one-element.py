class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        numsSum = sum(nums)

        if numsSum == n:
            return n-1
        elif numsSum == 0:
            return 0

        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        count1 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        return max(res)