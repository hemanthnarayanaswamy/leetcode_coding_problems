class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        count = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()
            for c in s[i+1:j]:
                between.add(c)
            count += len(between)
        
        return count
