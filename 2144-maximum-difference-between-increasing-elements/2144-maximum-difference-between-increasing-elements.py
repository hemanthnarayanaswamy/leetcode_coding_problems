class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        n = len(nums)

        l , r = 0, 1 

        while r < n:
            if nums[r] > nums[l]:
                d = nums[r] - nums[l]
                if d > maxDiff:
                    maxDiff = d
            else:
                l = r
            
            r += 1
        
        return maxDiff
