class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = []
        prefix = 0
        for num in nums:
            prefix+=num
            ans.append(prefix)
        return ans.count(0)