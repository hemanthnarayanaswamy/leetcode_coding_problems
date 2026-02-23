class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSet = set()
        n = len(s)
        reqCount = 2 ** k

        if k > n:
            return False

        for i in range(n - k + 1):
            codes = s[i:i+k]
            if codes not in uniqueSet:
                uniqueSet.add(codes)
                reqCount -= 1
            if reqCount == 0:
                return True
        
        return False