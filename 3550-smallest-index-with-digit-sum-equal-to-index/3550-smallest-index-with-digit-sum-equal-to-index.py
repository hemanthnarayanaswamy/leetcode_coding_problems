class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(x):
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total 

        for i, num in enumerate(nums):
            if i == digitSum(num):
                return i
        
        return -1