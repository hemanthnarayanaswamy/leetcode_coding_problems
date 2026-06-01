class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_good = [0]
        res = []

        for i in range(n-1):
            if nums[i+1] - nums[i] == 1:
                prefix_good.append(prefix_good[-1]+1)
            else:
                prefix_good.append(prefix_good[-1])
            
        left = 0 
        for right in range(k-1, n):
            if prefix_good[right] - prefix_good[left] >= k - 1:
                res.append(nums[right])
            else:
                res.append(-1)
            left += 1
            
        return res