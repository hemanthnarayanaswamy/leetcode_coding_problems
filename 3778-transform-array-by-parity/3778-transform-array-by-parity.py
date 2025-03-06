class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odds_count = 0
        for num in nums:
            if num % 2 == 1:
                odds_count += 1
        return [0]*(len(nums)-odds_count) + [1]*odds_count
            