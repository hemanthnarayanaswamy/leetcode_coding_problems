class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n)
        ans = set()

        for num, f in nFreq.items():
            if f < minFreq:
                minFreq = f
                ans.clear()
                ans.add(int(num))
            elif f == minFreq:
                ans.add(int(num))
        
        return min(ans)
