class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        val_count = nums.count(val)

        for i in range(val_count):
            nums.remove(val)
        
        return len(nums)
        