class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        rev = {}
        minDist = float('inf')

        for idx, num in enumerate(nums):
            if num in rev:
                dist = idx - rev[num]
                minDist = min(minDist, dist)
            numR = int(str(num)[::-1])
            rev[numR] = idx
        
        return -1 if minDist == float('inf') else minDist