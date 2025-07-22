class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        dist = 0

        for num in nums:
            dist += num 
            
            if dist == 0:
                res += 1
        
        return res
