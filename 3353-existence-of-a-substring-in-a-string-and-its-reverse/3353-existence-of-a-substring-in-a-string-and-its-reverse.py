class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        sRev = s[::-1]
        sl = 2

        for i in range(len(s)-1):
            if s[i:i+sl] in sRev:
                return True 
        
        return False