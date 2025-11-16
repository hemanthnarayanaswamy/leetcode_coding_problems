class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        run = 0
        
        for ch in s:
            if ch == '1':
                run += 1
            else:
                total += (run * (run+1)) // 2
                run = 0
                if total > MOD: 
                    total %= MOD
        
        total += (run * (run+1)) // 2

        return total % MOD