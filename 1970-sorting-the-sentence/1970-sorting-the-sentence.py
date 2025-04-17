class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        result = [' ']*len(s_list)

        for word in s_list:
            result[int(word[-1])-1] = word[:-1]
        return " ".join(result)