from collections import Counter 

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [key for key, value in Counter(nums).items() if value == 2]
        