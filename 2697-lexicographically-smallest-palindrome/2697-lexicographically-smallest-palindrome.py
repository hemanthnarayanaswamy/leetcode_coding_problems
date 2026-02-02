class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)

        while left < right:
            min_char = min(s[left], s[right])
            s[left] = s[right] = min_char

            left += 1
            right -= 1
        
        return ''.join(s)