class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSums = []
        tempSum = 0

        i = 0

        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                tempSum += nums[i]
            else:
                tempSum += nums[i]
                maxSums.append(tempSum)
                tempSum = 0
            
            i += 1
        
        if tempSum:
            tempSum += nums[i]
            maxSums.append(tempSum)
        else:
            maxSums.append(nums[i])
        
        return max(maxSums)
