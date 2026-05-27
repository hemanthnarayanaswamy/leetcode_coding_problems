class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charOccurrence = {}
        special_count = 0

        for i, c in enumerate(word):
            if c.isupper():
                if c not in charOccurrence:
                    charOccurrence[c] = i
            else:
                charOccurrence[c] = i
        
        for o in range(ord('a'), ord('z')+1):
            letter = chr(o)
            letterU = letter.upper()

            if letter in charOccurrence and letterU in charOccurrence:
                if charOccurrence[letter] < charOccurrence[letterU]:
                    special_count += 1
        
        return special_count