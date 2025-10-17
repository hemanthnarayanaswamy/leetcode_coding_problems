class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSet = set()
        n = len(s)

        for i in range(n - k + 1):
            codes = s[i:i+k]

            if codes not in uniqueSet:
                uniqueSet.add(codes)
        
        allcodes = 2 ** k

        return len(uniqueSet) == allcodes
            