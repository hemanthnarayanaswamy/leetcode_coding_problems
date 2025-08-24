class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swapCorrections = 2
        
        if Counter(s1) != Counter(s2):
            return False

        for c1,c2 in zip(s1, s2):
            if c1 != c2:
                swapCorrections -= 1
        
        return False if swapCorrections < 0 else True