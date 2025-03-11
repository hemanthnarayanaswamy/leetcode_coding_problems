class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        i = 0
        count = 1  # A number is always valid 

        for j in range(1, n):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                count = 1
            elif count < 2:
                nums[i + 1] = nums[j]
                i += 1
                count += 1
        return i + 1