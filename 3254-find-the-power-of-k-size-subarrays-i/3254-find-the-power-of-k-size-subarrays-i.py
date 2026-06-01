class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_good = []
        res = []

        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                prefix_good.append(1)
            else:
                prefix_good.append(0)
        
        print(prefix_good)
        l, r = 0, k-1
        while r < n:
            if sum(prefix_good[l:r]) == k-1:
                res.append(nums[r])
            else:
                res.append(-1)
            l += 1
            r += 1
        
        return res