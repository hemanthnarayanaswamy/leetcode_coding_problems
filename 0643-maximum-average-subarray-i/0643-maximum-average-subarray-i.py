class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])        # Compute the sum of the first window
        max_sum = current_sum              # Initialize max_sum with the first window sum

        # Slide the window from index 1 to n-k
        for i in range(k, len(nums)):                      # We have already calcluated the sum till K 
            current_sum += nums[i] - nums[i - k]  # Remove leftmost element, add new element
            max_sum = max(max_sum, current_sum)  # Update max_sum if the new sum is larger

        return max_sum / k  # Compute and return the maximum average

        