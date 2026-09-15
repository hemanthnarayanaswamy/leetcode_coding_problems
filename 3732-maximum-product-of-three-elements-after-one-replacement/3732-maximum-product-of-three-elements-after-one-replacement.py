class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res = 10**5
        
        l, r = 0, len(nums)-1
        count = 2

        while count:
            if abs(nums[l]) > abs(nums[r]):
                res *= nums[l]
                l += 1
            else:
                res *= nums[r]
                r -= 1
            count -= 1
        
        if res < 0:
            return -res
        else:
            return res
            
        


        
