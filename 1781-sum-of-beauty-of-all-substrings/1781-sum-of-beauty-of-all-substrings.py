class Solution:
    def beautySum(self, s: str) -> int:
        a = [ord(ch) - 97 for ch in s]
        n = len(a)
        total = 0

        for i in range(n):
            arr = [0] * 26
            maxC = 0
            for j in range(i, n):
                idx = a[j]
                arr[idx] += 1
                maxC = max(maxC, arr[idx])
                minC = min([val for val in arr if val != 0])
                total += (maxC - minC)
        
        return total