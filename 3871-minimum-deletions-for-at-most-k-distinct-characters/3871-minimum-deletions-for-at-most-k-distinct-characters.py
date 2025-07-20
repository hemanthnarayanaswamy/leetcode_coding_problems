class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        sFreq = sorted(Counter(s).values(), reverse=True)
        
        return sum(sFreq[k::])
        
