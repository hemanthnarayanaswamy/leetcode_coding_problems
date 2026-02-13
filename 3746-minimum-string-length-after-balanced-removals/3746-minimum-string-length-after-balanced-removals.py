class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        sFreq = Counter(s)

        return abs(sFreq.get('a', 0) - sFreq.get('b', 0))

