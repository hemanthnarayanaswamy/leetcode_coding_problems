class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        fillCount = len(s) % k
        n = len(s)
        result = []
        
        if fillCount:
            s += (n - fillCount + k) * fill
        
        for i in range(0, n, k):
            result.append(s[i:i+k])
        
        return result
        

