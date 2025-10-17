class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniqueSet = set()

        for i in range(len(s)):
            codes = s[i:i+k]
            
            if codes not in uniqueSet and len(codes) == k:
                uniqueSet.add(codes)
        
        allcodes = 2 ** k

        return len(uniqueSet) == allcodes
            