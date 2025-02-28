class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return ''
                r -= 1
                l += 1
            return s 
        
        for word in words: 
            if is_palindrome(word):
                return word
        return ''
        