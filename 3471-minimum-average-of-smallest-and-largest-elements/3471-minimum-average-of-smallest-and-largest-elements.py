class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        averages = []
        l, r = 0, len(nums)-1

        while l < r:
            avg = (nums[l]+nums[r])/2
            averages.append(avg)
            l += 1
            r -= 1
        
        return min(averages)