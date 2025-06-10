class Solution:
    def maxDifference(self, s: str) -> int:
        OddMax, EvenMin = 0, 100

        for v in Counter(s).values():
            if v % 2 == 0:
                EvenMin = min(EvenMin, v)
            else:
                OddMax = max(OddMax, v)
        
        return OddMax - EvenMin