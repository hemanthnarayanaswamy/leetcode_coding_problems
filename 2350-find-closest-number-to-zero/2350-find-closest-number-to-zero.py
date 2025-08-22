class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = float('inf')
        res = nums[0]

        for num in nums:
            if abs(num) < diff or (abs(num) == diff and num > res):
                res = num
                diff = abs(num)
    
        return res