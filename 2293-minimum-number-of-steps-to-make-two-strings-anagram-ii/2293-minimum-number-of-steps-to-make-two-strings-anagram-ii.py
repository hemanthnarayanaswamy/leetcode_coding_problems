class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operations = 0
        sFreq = Counter(s)
        tFreq = Counter(t)

        for c in sFreq:
            if sFreq[c] < tFreq.get(c, 0):
                operations += tFreq.get(c, 0) - sFreq[c]
            elif c not in tFreq:
                operations += sFreq[c]
        
        for c in tFreq:
            if tFreq[c] < sFreq.get(c, 0):
                operations += sFreq.get(c, 0) - tFreq[c]
            elif c not in sFreq:
                operations += tFreq[c]

        return operations
