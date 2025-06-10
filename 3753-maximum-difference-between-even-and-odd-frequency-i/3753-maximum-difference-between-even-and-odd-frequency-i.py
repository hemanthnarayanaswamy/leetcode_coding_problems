class Solution:
    def maxDifference(self, s: str) -> int:
        sFreq = [val for val in Counter(s).values()]

        OddMax, EvenMin = 0, 100

        for v in sFreq:
            if v % 2 == 0:
                EvenMin = min(EvenMin, v)
            else:
                OddMax = max(OddMax, v)
        
        return OddMax - EvenMin