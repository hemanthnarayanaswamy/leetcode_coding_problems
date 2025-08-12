class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        max_val, min_val = max(nums), min(nums)

        for num in nums:
            if min_val < num < max_val:  
                count += 1
        
        return count