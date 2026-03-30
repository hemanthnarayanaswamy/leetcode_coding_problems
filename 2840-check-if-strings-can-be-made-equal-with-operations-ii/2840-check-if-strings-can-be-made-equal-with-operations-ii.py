class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        
        odds1 = s1[1:n:2]
        evens1 = s1[0:n:2]
        odds2 = s2[1:n:2]
        evens2 = s2[0:n:2]
        
        if len(odds1) != len(odds2) or len(evens1) != len(evens2) or Counter(odds1) != Counter(odds2) or Counter(evens1) != Counter(evens2):
            return False
        
        return True