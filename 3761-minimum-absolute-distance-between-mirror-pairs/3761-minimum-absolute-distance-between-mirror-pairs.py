class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        n = len(nums)
        minDist = float('inf')

        for i, num in enumerate(nums):
            pos[num].append(i)

        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])      
            if rev not in pos:
                continue
            
            indices = pos[rev]                 # all j where nums[j] == rev
            k = bisect_right(indices, i)       # first j > i

            if k < len(indices):
                j = indices[k]
                minDist = min(minDist, j - i)
        
        return -1 if minDist == float('inf') else minDist