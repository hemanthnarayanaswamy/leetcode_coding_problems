class Solution:
    def maxDifference(self, s: str) -> int:
        OddMax  = 0
        EvenMin = float('inf')

        for v in Counter(s).values():
            if v % 2:
                OddMax = max(OddMax, v)
            else:
                EvenMin = min(EvenMin, v)
        
        return OddMax - EvenMin