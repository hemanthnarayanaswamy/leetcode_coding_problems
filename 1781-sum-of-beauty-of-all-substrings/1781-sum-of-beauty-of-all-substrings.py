class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            arr = [0] * 26
            maxC = 0
            for j in range(i, n):
                idx = ord(s[j])-97
                arr[idx] += 1
                maxC = max(maxC, arr[idx])
                minC = min([val for val in arr if val != 0])
                total += (maxC - minC)
        
        return total