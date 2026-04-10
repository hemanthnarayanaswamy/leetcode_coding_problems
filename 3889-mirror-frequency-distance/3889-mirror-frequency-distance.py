class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        mirrorFreq = defaultdict(int)



        for c in s:
            if c.isnumeric():
                mir = str(9 - int(c))
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))

            pair = (c, mir) if c > mir else (mir, c) # we generate character and mirror pair in sorted order

            if pair not in mirrorFreq: # If the pair is unique only find the absolute difference
                mirrorFreq[pair] = abs(freq[mir] - freq[c])
        
        return sum(mirrorFreq.values()) # We need to return the sum of absolute difference of all unique pairs
            