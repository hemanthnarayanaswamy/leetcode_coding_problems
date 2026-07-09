class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)

        if n < k:
            return False
        if k == n:
            return True

        oddCount = 0

        for v in Counter(s).values():
            if v % 2 == 1:
                oddCount += 1
            
            if oddCount > k:
                return False
        
        return True
        
