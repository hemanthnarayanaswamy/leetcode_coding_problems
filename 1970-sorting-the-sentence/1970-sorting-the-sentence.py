class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        result = [0]*len(s_list)

        for word in s_list:
            result[int(word[-1])-1] = word[:len(word)-1]
        return " ".join(result)