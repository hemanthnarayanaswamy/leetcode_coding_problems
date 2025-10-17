class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSet = set()
        n = len(s)
        allcodesCount = 2 ** k
        count = 0 

        for i in range(n - k + 1):
            codes = s[i:i+k]
            if codes not in uniqueSet:
                uniqueSet.add(codes)
                count += 1
            if count == allcodesCount:
                return True
        
        return count == allcodesCount
