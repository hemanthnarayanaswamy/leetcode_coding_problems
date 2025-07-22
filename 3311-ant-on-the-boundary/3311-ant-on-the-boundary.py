class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        for num in nums:
            prefix+=num
            if prefix == 0:
                ans+=1
        return ans