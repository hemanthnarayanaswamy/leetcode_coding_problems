class Solution:
    def numSub(self, s: str) -> int:
        totalSubstrings = 0
        onesCount = 0
        MOD = 10**9 + 7

        for c in s:
            if c == '1':
                onesCount += 1
            else:
                totalSubstrings += (onesCount * (onesCount + 1))// 2
                onesCount = 0
        
        totalSubstrings += (onesCount * (onesCount + 1))// 2

        return totalSubstrings % MOD