from collections import Counter 

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_freq = Counter(nums)

        for num in nums_freq:
            if nums_freq[num] % 2 != 0:
                return False 
        
        return True
        