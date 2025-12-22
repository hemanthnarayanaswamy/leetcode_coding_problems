class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver = []
        prefix = [0]
        currentMax = nums[0]

        for i in range(len(nums)):
            if currentMax < nums[i]:
                currentMax = nums[i]

            conver.append(prefix[-1] + nums[i] + currentMax)
            prefix.append(prefix[-1] + nums[i] + currentMax)
        
        return conver