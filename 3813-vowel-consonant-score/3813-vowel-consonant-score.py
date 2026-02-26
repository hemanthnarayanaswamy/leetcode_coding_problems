class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        v = c = 0

        for chr in s:
            if chr in vowels:
                v += 1
            elif chr.isalpha():
                c += 1
        
        return floor(v/c) if c > 0 else 0
