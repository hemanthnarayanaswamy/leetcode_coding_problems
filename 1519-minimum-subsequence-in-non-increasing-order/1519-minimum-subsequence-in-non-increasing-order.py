class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        totalsum = sum(nums)
        nums.sort(reverse=True)
        res = []
        tmp = 0

        for n in nums:
            tmp += n 
            if tmp <= totalsum - n:
                res.append(n)
                totalsum -= n
            else:
                res.append(n)
                return res
        
        return res
            
