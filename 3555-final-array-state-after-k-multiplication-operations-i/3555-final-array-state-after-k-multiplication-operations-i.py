class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        for _ in range(k):
            # find the index of the minimum element
            min_idx = 0
            for i in range(1, n):
                if nums[i] < nums[min_idx]:
                    min_idx = i
            # multiply that minimum
            nums[min_idx] *= multiplier
        return nums
