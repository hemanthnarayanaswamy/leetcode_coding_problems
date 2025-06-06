class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sFreq = Counter(s)
        tFreq = Counter(t)
        print(sFreq, tFreq)

        for char in tFreq:
            if char not in sFreq:
                return char
            
            if tFreq[char] != sFreq[char]:
                return char