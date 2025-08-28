class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 1

        while i < len(nums)-1:
            x, y = nums[i], nums[i+1]
            nums[i] = y
            nums[i+1] = x
            i += 2
        
        return nums
