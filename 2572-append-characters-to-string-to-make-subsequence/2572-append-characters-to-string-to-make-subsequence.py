class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si, ti = 0, 0
        
        # Try to match as many characters of t in s as possible
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1  # Found a match, move to next char in t
            si += 1  # Always move forward in s
        
        # Return the number of characters from t that still need to be appended
        return len(t) - ti