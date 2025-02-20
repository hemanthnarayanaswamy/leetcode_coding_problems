class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found_nums = {} ## HAsh Map to track the number

        if len(nums) == len(set(nums)): ## A small edge case to resolve much faster
            return False

        for i,num in enumerate(nums):
            if num in found_nums and abs(i-found_nums[num]) <= k: # checking conditions 
                return True 
                ## Removed the else block
            found_nums[num] = i
        return False
        