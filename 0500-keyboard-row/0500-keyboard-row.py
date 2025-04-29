class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            lower_word = word.lower()
            if all(char in keyboard[0] for char in lower_word):
                res.append(word)
            elif all(char in keyboard[1] for char in lower_word):
                res.append(word)
            elif all(char in keyboard[2] for char in lower_word):
                res.append(word)
        return res
                    



        