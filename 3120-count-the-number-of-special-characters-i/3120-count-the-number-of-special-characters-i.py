class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        searchWord = set(word)
        count = 0

        for code in range(ord('a'), ord('z') + 1):
            c = chr(code)

            if c in searchWord and c.upper() in searchWord:
                count += 1
        
        return count
