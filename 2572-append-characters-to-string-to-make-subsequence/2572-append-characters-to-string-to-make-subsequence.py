class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si, ti = 0, 0

        if s == t:
            return 0
        
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1  
            si += 1  
        
        return len(t) - ti