class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total 

        for i, num in enumerate(nums):
            if i == digitSum(num):
                return i
        
        return -1