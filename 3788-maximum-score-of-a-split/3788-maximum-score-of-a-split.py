class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        suff, pref = nums.pop(), sum(nums)  
        ans = float('-inf')

        while nums:  
            tmp = pref - suff                       
            if  ans < tmp: 
                ans = pref - suff

            num = nums.pop()
            pref-= num     
                              
            if  suff > num:
                suff = num      

        return ans
    