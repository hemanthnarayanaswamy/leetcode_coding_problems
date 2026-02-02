class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r =  0, len(s)-1
        s = list(s)

        while l < r:
            c1 = s[l]
            c2 = s[r]
            if c1 != c2:
                if c1 < c2:
                    s[r] = c1
                else:
                    s[l] = c2
            l += 1
            r -= 1
        
        return ''.join(s)