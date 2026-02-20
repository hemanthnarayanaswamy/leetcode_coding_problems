class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(c1, c2):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c == c1 or c == c2:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)

        for i in range(1, len(s)):
            if characters[i] == '?':
                if i == len(s)-1:
                    c1 = c2 = characters[i-1]
                else:
                    c1 = characters[i-1]
                    c2 = characters[i+1]

                characters[i] = replacement(c1, c2)
        
        if characters[0] == '?':
            if len(s) == 1:
                return 'a'
            else:
                c1 = c2 = characters[1]
                characters[0] = replacement(c1, c2)

        
        return ''.join(characters)

