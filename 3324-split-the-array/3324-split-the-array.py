class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = nums_map.get(nums[i], 0) + 1
        
        # if len(nums_map) == 1:
        #     return False
        
        for key in nums_map:
            if nums_map[key] > 2:
                return False
        return True

        