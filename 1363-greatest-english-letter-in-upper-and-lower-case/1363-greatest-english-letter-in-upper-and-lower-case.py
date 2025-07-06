class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        seen = set(s)

        for c in alphabets[::-1]: # check from 'Z' down to 'A'
            if c in seen and c.lower() in seen:
                return c

        return ''
