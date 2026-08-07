class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        maxProd = float('-inf')

        suffixMax = [0]*n
        suffixMin = [0]*n

        suffixMax[-1] = suffixMin[-1] = nums[-1]


        for i in range(n-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], nums[i])
            suffixMin[i] = min(suffixMin[i+1], nums[i])

        for i in range(n-m+1):
            if nums[i] > 0:
                p = nums[i] * suffixMax[i+m-1]
            else:
                p = nums[i] * suffixMin[i+m-1]
            
            if p > maxProd:
                maxProd = p
        
        return maxProd