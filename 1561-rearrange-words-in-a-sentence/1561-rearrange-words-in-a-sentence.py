class Solution:
    def arrangeWords(self, s: str) -> str:
        return " ".join(sorted(s.split(),key=len)).lower().capitalize()
        