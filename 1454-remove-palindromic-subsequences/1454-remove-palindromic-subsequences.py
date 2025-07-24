class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def checkPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False 
            return True
        
        return 1 if checkPalindrome(s) else 2