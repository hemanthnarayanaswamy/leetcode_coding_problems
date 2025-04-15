class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s =list(s)
        l, r = 0, len(s)-1 

        while l < r:
            asc_l = ord(s[l])
            asc_r = ord(s[r])
            if asc_l in range(65,91) or asc_l in range(97,123):
                if asc_r in range(65,91) or asc_r in range(97,123):
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
        
        return ''.join(s)
        