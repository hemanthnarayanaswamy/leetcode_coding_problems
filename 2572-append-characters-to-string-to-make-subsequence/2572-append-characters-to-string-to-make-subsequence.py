class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        char_count = 0
        si, ti = 0, 0

        while ti < len(t):
            if s[si] == t[ti]:
                ti += 1
                
            si += 1
            
            if si == len(s):
                return len(t[ti:])
        
        return 0
