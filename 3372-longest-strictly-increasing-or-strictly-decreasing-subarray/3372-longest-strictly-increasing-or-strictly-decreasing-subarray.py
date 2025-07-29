class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res, res_inc, res_dec = 1, 1, 1

        i = 1

        while i < len(nums):
            if nums[i-1] > nums[i]:
                res_inc += 1
                res_dec = 1
            elif nums[i-1] < nums[i]:
                res_dec += 1
                res_inc = 1
            else:
                res_dec = 1
                res_inc = 1
            
            res = max(res, res_dec, res_inc)
            i += 1
        
        return res
            
