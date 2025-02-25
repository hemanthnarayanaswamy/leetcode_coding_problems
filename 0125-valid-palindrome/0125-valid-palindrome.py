class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for char in s.lower():
            if char.isalnum():
                s2 += char
        
        return s2 == s2[::-1]
        