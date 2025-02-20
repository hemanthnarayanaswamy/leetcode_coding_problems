class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found_nums = {} ## HAsh Map to track the number
        
        for i,num in enumerate(nums):
            if num in found_nums and abs(i-found_nums[num]) <= k: # checking conditions 
                return True 
            else:
                found_nums[num] = i
        return False
        