class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sFreq = Counter(s)
        tFreq = Counter(t)

        for char in tFreq:
            if sFreq.get(char, 0) != tFreq.get(char):
                return char