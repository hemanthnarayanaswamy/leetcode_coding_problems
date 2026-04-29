class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1
                maxC = max(freq.values())
                minC = min(freq.values())
                total += (maxC - minC)
        
        return total
