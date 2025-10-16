class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sNew = s.replace('-', '')[::-1]
        n = len(sNew)

        if n == 0 or n < k:
            return sNew.upper()[::-1]
        
        res = []

        for i in range(n):
            if i != 0 and i % k == 0:
                res.append('-')
            res.append(sNew[i].upper())
        
        return ''.join(res)[::-1]