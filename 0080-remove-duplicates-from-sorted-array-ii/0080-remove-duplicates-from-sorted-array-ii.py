class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:   ## If nums has 2 or fewer elements, all are already valid
            return n
    
        slow = 2     ## Since the first two index are always valid 

        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]    ## Overwrite the element at 'slow' index
                slow += 1
        return slow
            