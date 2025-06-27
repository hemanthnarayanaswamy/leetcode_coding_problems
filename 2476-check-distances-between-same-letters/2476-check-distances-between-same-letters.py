class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        charDist = {}

        for i, chr in enumerate(s):
            charDist[chr] = i - charDist.get(chr, 0)
        
        for c in charDist:
            if charDist[c] - 1 != distance[ord(c)-97]:
                return False
        
        return True
