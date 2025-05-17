class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        fh, sh = 0, 0

        l, r = 0, len(s)-1

        while l < r:
            if s[l] in vowels:
                fh += 1
            
            if s[r] in vowels:
                sh += 1
            
            l += 1
            r -= 1
        
        return fh == sh