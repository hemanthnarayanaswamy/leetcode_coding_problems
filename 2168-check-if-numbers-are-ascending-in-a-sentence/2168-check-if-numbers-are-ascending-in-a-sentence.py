class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [char for char in s.split() if char.isnumeric()]
        
        for i in range(1, len(nums)):
            if int(nums[i]) <= int(nums[i-1]):
                return False 
        
        return True

