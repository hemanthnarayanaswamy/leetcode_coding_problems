class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        #ans = [0]*len(nums)
        n = len(nums)

        # for i in range(len(nums)):
        #     ans[i] = nums[nums[i]]
        
        return [nums[nums[i]] for i in range(n)]
        