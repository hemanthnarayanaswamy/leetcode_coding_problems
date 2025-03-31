class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major_condition = len(nums) // 3
        return [key for key, value in Counter(nums).items() if value > major_condition]