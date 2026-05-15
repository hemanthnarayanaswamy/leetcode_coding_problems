class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        count = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            count += len(set(s[i+1: j]))
        
        return count