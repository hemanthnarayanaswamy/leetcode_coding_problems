class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        totalMax = 0

        for i in range(n - 2):
            for j in range(i+1, n -1):
                for k in range(j+1, n):
                    total = (nums[i] - nums[j]) * nums[k]
                    totalMax = max(total, totalMax)
        
        return totalMax