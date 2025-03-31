from collections import Counter 

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        return [key for key, value in nums_freq.items() if value == 2]
        