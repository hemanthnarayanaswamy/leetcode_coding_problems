class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minNum = min(nums)
        if minNum < k:
            return -1

        n = len(set(nums))

        return n if minNum != k else n-1 
