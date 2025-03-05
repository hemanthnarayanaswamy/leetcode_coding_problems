class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count, max_count = 0, 0
        for num in nums:
            if num == 1:
                current_count += 1  # Increment count for consecutive 1s
            else:
                max_count = max(max_count, current_count)  # Update max before resetting
                current_count = 0  # Reset counter on encountering 0

        return max(max_count, current_count)  # Final check for ending with 1s
