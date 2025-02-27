class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0 

        for start in range(len(nums)):
            if nums[start] != 0:
                nums[p1], nums[start] = nums[start], nums[p1]
                p1 += 1
       
            