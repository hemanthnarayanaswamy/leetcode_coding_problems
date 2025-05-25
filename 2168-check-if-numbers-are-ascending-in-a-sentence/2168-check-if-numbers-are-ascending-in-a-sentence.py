class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(char) for char in s.split() if char.isnumeric()]
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                return False 
        
        return True