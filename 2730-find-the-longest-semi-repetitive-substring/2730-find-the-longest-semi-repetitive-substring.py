class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            return n

        left = maxLen = repeat= 0 

        for right in range(1, n):
            if s[right-1] == s[right]:
                repeat += 1
            
            while repeat > 1:
                if s[left] == s[left + 1]:
                    repeat -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen


