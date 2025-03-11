class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:  # If nums has 2 or fewer elements, all are already valid
            return len(nums)

        slow = 2  # Start writing from index 2 (since first 2 elements are always valid)
        
        for fast in range(2, len(nums)):  # Start scanning from index 2
            if nums[fast] != nums[slow - 2]:  # Allow at most 2 occurrences
                nums[slow] = nums[fast]  # Overwrite the element at 'slow' index
                slow += 1  # Move write pointer forward
        
        return slow  # 'slow' represents the new length of the modified array
