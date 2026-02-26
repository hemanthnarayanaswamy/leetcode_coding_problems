class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = 'aeiou'
        v = c = 0

        for chr in s:
            if chr in vowels:
                v += 1

            if chr.isalpha():
                c += 1
        
        return 0 if c == v else floor(v/(c-v))
