class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        result = ['']*len(s)

        for word in s:
            result[int(word[-1])-1] = word[:-1]
        return " ".join(result)