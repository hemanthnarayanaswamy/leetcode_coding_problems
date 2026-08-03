class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        ans = 0
        n = len(nums)
        # A subarray with y > 0 is valid exactly when b * x <= a * y

        for i in range(n):
            x = y = 0
            for j in range(i, n):
                if nums[j] % 2:
                    y += 1
                else: 
                    x += 1
                
                if y == 0:
                    continue
                
                if b * x <= a * y:
                    ans += 1
        
        return ans


