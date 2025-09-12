class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        start = 0
        totalSum = 0

        for i, num in enumerate(nums):
            totalSum += num 

            newStart = max(0 , i - num)
            if newStart > start:
                totalSum -= sum(nums[start:newStart])
                start = newStart
            elif 0 <= newStart < start:
                totalSum += sum(nums[newStart:start])
                start = newStart
            
            res += totalSum
        
        return res


