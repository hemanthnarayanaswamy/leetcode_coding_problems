class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        result = []
        for word in s:
            word = [letter for letter in word]
            l, r = 0, len(word)-1
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            
            result.append("".join(word))
        return " ".join(result)