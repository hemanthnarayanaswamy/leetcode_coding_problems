class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Extract even-indexed and odd-indexed elements
        evens = sorted(nums[::2])                      # ascending
        odds  = sorted(nums[1::2], reverse=True)       # descending

        # Allocate result array of the same length
        res = [None] * len(nums)
        # Place sorted values back into even and odd positions
        res[::2] = evens
        res[1::2] = odds

        return res
