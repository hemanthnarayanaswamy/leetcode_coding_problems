class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        m = n // 2 
        newNum = nums

        while m:
            temp = [0]*m 

            for i in range(m):
                if i % 2:
                    temp[i] = max(newNum[2*i], newNum[2*i + 1])
                else:
                    temp[i] = min(newNum[2*i], newNum[2*i + 1])
            
            newNum = temp
            m //= 2
        
        return newNum[0]