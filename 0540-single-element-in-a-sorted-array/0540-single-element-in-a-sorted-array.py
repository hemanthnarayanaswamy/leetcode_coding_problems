class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even for consistent checking
            if mid % 2 == 1:
                mid -= 1
            
            # Check if the pair is intact
            if nums[mid] == nums[mid + 1]:
                # Pair is intact, single element is on the right
                left = mid + 2
            else:
                # Pair is broken, single element is on the left (or at mid)
                right = mid
        
        return nums[left]