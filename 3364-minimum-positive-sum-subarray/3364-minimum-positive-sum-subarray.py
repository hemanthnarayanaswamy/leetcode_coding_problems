class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        subSum = 0
        minSum = float('inf')
        prefix = [0]

        for i in range(n):
            prefix.append(prefix[-1]+nums[i])
        
        for i in range(n):
            for r in range(l, r+1):
                if i + r > n:
                    break
                
                subSum = prefix[i+r] - prefix[i]

                if subSum > 0 and subSum < minSum:
                    minSum = subSum
        
        return minSum if minSum != float('inf') else -1