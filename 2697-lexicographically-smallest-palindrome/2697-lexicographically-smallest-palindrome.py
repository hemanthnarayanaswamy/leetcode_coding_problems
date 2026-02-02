class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l, r =  0, len(s)-1
        s = list(s)

        while l < r:
            c1 = s[l]
            c2 = s[r]
            if c1 != c2:
                o1 = ord(c1)
                o2 = ord(c2)
                if o1 < o2:
                    s[r] = c1
                else:
                    s[l] = c2
            l += 1
            r -= 1
        
        return ''.join(s)