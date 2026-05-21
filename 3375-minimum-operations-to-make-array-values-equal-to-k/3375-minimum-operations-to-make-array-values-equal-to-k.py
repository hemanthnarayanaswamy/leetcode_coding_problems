class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        if min_num >= k:
            return len(set(nums)) - (min_num == k)
        return -1
        