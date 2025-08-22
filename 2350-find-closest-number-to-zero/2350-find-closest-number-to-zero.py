class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = float('inf')
        res = 0

        for num in nums:
            if abs(num) < diff:
                res = num 
                diff = abs(num)
            if abs(num) == diff and num > res:
                res = num
        
        return res