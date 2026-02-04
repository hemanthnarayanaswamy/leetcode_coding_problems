class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                a, b = nums[i], nums[j]
                if a >= b:
                    break
                for k in range(j+1, n):
                    c = nums[k]
                    if c >= b or (a+b+c) >= res:
                        continue
                    res = a+b+c
        
        return res if res != float('inf') else -1
