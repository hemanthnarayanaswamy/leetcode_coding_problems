class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSet = set()
        n = len(s)
        count = 0 

        for i in range(n - k + 1):
            codes = s[i:i+k]

            if codes not in uniqueSet:
                uniqueSet.add(codes)
                count += 1
        
        allcodesCount = 2 ** k

        return count == allcodesCount
