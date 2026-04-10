class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        mirrorFreq = defaultdict(int)

        for c in s:
            if c.isnumeric():
                mir = str(9 - int(c))
                f = abs(freq[mir] - freq[c])
                k = (c, mir) if c > mir else (mir, c)
                mirrorFreq[k] = f
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))
                f = abs(freq[mir] - freq[c])
                k = (c, mir) if c > mir else (mir, c)
                mirrorFreq[k] = f
        
        return sum(mirrorFreq.values())
            