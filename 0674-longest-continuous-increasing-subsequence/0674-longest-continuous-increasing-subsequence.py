class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen = 1
        currLen = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                currLen += 1
            else:
                maxLen = max(maxLen, currLen)
                currLen = 1
                
        maxLen = max(maxLen, currLen)
        
        return maxLen