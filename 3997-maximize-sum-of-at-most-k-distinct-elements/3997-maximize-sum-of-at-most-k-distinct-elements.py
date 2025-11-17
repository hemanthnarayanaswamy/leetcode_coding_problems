class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        distinctNums = sorted(set(nums), reverse=True)

        return distinctNums[:k]