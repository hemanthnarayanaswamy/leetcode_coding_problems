class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letterCount = s.count(letter)
        n = len(s)
        percentage = (letterCount / n) * 100

        return int(percentage)