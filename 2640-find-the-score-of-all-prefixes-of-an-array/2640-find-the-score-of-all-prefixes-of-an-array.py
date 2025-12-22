class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        conver = []
        prefix = 0
        currentMax = nums[0]

        for num in nums:
            if num > currentMax:
                currentMax = num
            score = prefix + num + currentMax
            conver.append(score)
            prefix = score
        
        return conver