class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sFreq = Counter(s)
        tFreq = Counter(t)

        # Compute the Freq of the both strings and compare the values and return the char that has mis matched values.
        for char in tFreq:
            if sFreq.get(char, 0) != tFreq.get(char):
                return char