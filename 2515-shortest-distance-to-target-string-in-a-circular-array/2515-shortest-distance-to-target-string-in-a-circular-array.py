class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        shortDistance = float('inf')

        for i in range(startIndex, n+startIndex):
            i = i % n
            if words[i] == target:
                dist = abs(startIndex - i)
                shortDistance = min(shortDistance, dist, n - dist)
        
        return -1 if shortDistance == float('inf') else shortDistance
