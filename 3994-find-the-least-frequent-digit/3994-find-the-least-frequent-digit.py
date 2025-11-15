class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n)

        for f in nFreq.values():
            if f < minFreq:
                minFreq = f

        ans = []
        for num,f in nFreq.items():
            if f == minFreq:
                ans.append(int(num))
        
        return min(ans)
