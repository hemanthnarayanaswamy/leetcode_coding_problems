class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = sum(nums[:2])
        operations = 1
        n = len(nums)

        if n%2:
            n -= 1

        for i in range(2, n, 2):
            if sum(nums[i:i+2]) != score:
                break
            
            operations += 1
        
        return operations
