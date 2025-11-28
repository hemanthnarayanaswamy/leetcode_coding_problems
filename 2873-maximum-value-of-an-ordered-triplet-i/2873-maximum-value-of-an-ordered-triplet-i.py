class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        totalMax = 0
        diffMax = 0

        for i in range(n - 2):
            for j in range(i+1, n -1):
                diff = nums[i] - nums[j]
                for k in range(j+1, n):
                    total = diff * nums[k]
                    if total > totalMax:
                        totalMax = total 
        
        return totalMax