class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = {}
        ans = float('inf')

        for idx, val in enumerate(nums):
            if val in res:
                ans = min(ans, idx - res[val])
            res[int(str(val)[::-1])] = idx
        
        return -1 if ans == float('inf') else ans