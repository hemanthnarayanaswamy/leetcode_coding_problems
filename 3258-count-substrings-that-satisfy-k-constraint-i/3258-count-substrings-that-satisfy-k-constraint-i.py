class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zeroCount = oneCount = 0
        res = 0
        start = 0

        for i in range(len(s)):
            if s[i] == '1':
                oneCount += 1
            else:
                zeroCount += 1
            
            while zeroCount > k and oneCount > k:
                if s[start] == '1':
                    oneCount -= 1
                else:
                    zeroCount -= 1
                start += 1
            res += i - start + 1
        
        return res