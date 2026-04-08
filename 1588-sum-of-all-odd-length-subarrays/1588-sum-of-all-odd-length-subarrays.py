class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totalSum = 0
        n = len(arr)

        for i, num in enumerate(arr):
            sub = (((i+1)*(n-i)) + 1) // 2
            totalSum += num * sub
        
        return totalSum