class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        mirrorFreq = set()
        total = 0

        for c in freq.keys():
            if c.isnumeric():
                mir = str(9 - int(c))
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))

            pair = (c, mir) if c > mir else (mir, c) # we generate character and mirror pair in sorted order

            if pair not in mirrorFreq: # If the pair is unique only find the absolute difference
                total += abs(freq[mir] - freq[c])
                mirrorFreq.add(pair) 
        
        return total # We need to return the sum of absolute difference of all unique pairs
            