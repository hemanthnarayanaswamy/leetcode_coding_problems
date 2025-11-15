class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n)
        ans = []

        for num, f in nFreq.items():
            if f < minFreq:
                minFreq = f
                ans.clear()
                ans.append(int(num))
            elif f == minFreq:
                ans.append(int(num))
        
        return min(ans)
