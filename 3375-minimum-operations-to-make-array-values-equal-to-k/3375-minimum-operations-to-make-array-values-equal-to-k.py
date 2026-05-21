class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minNum = min(nums)
        if minNum < k:
            return -1

        nums = set(nums)
        n = len(nums)

        if minNum != k:
            return n
        else: 
            return n-1
        
