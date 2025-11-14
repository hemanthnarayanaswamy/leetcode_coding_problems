class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float('inf')
        numsMap = defaultdict(list)

        for i in range(len(nums)):
            numsMap[nums[i]].append(i)
            n = len(numsMap[nums[i]]) 
            if n >= 3:
                if n > 3:
                    numsMap[nums[i]].pop(0)

                l = numsMap[nums[i]][0]
                res = min(res, 2*(i - l))
            
        return res if res != float('inf') else -1
            