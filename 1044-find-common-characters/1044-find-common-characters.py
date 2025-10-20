class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        c = Counter(words[0])

        for w in words[1:]:
            c &= Counter(w)           # min per character
              
        return list(c.elements())     # expand by counts