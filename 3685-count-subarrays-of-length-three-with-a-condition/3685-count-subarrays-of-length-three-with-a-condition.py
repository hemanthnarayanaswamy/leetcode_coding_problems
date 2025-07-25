class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            x,y,z = nums[i], nums[i+1], nums[i+2]

            if float(x + z) == float(y/2):
                count += 1
        
        return count