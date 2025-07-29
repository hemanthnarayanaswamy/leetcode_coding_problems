class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operations = 0
        sFreq = Counter(s)
        tFreq = Counter(t)

        for i in range(97, 123):
            c = chr(i)
            if c in sFreq and c not in tFreq:
                operations += sFreq[c]
            elif c in tFreq and c not in sFreq:
                operations += tFreq[c]
            else:
                operations += abs(sFreq.get(c, 0) - tFreq.get(c, 0))
        
        return operations