class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i,num in enumerate(nums):
            if nums[i] > 0:
                j = (i+nums[i]) % n
                res[i] = nums[j]
            else:
                j = (i + nums[i]) % n
                res[i] = nums[j]
        
        return res