class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s =list(s)
        l, r = 0, len(s)-1 

        while l < r:
            if s[l].isalpha():
                if s[r].isalpha():
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        
        return ''.join(s)
        