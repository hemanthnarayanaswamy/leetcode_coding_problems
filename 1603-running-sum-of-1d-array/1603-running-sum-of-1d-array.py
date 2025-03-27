class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            result[i] = prefix
        
        return result