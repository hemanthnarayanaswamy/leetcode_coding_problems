class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sNew = s.replace('-', '')[::-1]
        res = []

        for i in range(len(sNew)):
            if i % k == 0 and i != 0:
                res.append('-')
            
            res.append(sNew[i].upper())
        print(res)
        return ''.join(res)[::-1]