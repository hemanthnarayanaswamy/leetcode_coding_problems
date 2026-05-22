class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        left = 0 
        max_len = 0

        for right in range(len(nums)):
            if nums[right]>threshold:
                left = right+1
                continue
            if (left == right and nums[right] % 2 == 0) or (right > left and nums[right] % 2 != nums[right - 1] % 2):
                max_len = max(max_len, right - left + 1)
            else:
                if nums[right] % 2 == 0:
                    left = right
                    max_len = max(max_len, 1)
                else:
                    left = right+1
        return max_len