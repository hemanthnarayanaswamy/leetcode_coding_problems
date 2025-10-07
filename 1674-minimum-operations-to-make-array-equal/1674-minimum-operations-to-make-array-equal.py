class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2*i)+1 for i in range(n)]
        count = 0
        target = sum(arr) // n

        for i in arr:
            if i < target:
                count += target - i 
        
        return count
