class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        length = False
        low = False
        up = False
        digit = False
        special = False
        specialChars = "!@#$%^&*()-+"
        prev = ''

        n = len(password)

        if n >= 8:
            length = True

        for c in password:
            if c == prev:
                return False
            elif c.islower():
                low = True
            elif c.isupper():
                up = True
            elif c.isdigit():
                digit = True
            elif c in specialChars:
                special = True
            prev = c

        return length and low and up and special and digit