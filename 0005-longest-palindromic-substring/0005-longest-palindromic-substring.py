class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # Extract palindrome substring

        longest = ""
        
        for i in range(len(s)):
            # Expand for odd-length palindromes (single-character center)
            odd_palindrome = expandAroundCenter(i, i)
            # Expand for even-length palindromes (two-character center)
            even_palindrome = expandAroundCenter(i, i + 1)

            # Update longest palindrome found
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest
