class Solution:
    def scoreBalance(self, s: str) -> bool:
        prefixSum = [0] * len(s)
        prev = 0

        for i in range(len(s)):
            prefixSum[i] = prev + (ord(s[i]) - 96)
            prev = prefixSum[i]
        
        totalVal = prefixSum[-1]

        for s in prefixSum:
            if s == (totalVal - s):
                return True
                
        return False
            