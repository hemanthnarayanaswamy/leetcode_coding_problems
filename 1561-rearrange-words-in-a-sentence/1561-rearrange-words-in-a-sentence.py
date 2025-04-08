class Solution:
    def arrangeWords(self, text: str) -> str:
        # return " ".join(sorted(text.split(),key=len)).lower().capitalize()
        words = text.split(' ')
        words.sort(key = lambda x: len(x))

        res = " ".join(words)
        res = res.lower()
        return res[0].upper() + res[1:]
        