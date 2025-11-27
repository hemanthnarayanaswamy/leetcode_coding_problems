class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for i,num in enumerate(nums):
                j = (i + num) % n
                res.append(nums[j])
        
        return res