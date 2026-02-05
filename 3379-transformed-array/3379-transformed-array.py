class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i,num in enumerate(nums):
                res.append(nums[(i + num) % n])
        
        return res