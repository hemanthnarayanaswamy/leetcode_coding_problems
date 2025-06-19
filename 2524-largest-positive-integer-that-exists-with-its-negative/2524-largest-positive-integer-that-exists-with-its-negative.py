class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        larNum = -1 

        seen = set()

        for num in nums:
            if -num in seen:
                if abs(num) > larNum:
                    larNum = abs(num)
            
            seen.add(num)
        
        return larNum

            