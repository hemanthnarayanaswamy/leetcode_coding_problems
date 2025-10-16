class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sNew = s.replace('-', '')[::-1]
        n = len(sNew)

        if n == 0:
            return ""
        elif n <= k:
            return sNew[::-1].upper()   
        
        parts = [sNew[i:i+k] for i in range(0, n, k)]
        formattedKey = '-'.join(parts)[::-1].upper()
        return formattedKey 