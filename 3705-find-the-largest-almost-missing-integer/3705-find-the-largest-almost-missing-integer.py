from collections import Counter 

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nums_freq = Counter(nums)
        n = len(nums)

        # Case 1: If k == 1, return largest unique number (frequency == 1)
        if k == 1:
            max_unique = -1
            for num, freq in nums_freq.items():
                if freq == 1 and num > max_unique:
                    max_unique = num
            return max_unique

        # Case 2: If k == length of nums, just return the max
        if k == n:
            return max(nums)

        # Case 3: If 1 < k < n, custom logic
        count_first = nums_freq[nums[0]]
        count_last = nums_freq[nums[-1]]

        if count_first > 1 and count_last > 1:
            return -1
        elif count_first > 1:
            return nums[-1]
        elif count_last > 1:
            return nums[0]
        else:
            return max(nums[0], nums[-1])