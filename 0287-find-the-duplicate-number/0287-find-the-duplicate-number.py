class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniq = set()

        for i in range(len(nums)):
            if nums[i] in uniq:
                return nums[i]
            else:
                uniq.add(nums[i])