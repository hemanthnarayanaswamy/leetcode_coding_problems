class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(avoid):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c in avoid:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)
        n = len(s)

        for i in range(1, n):
            if characters[i] == '?':
                if i != n-1:
                    avoid = characters[i-1] + characters[i+1]
                else:
                    avoid = characters[i-1]

                characters[i] = replacement(avoid)
        
        if characters[0] == '?':
            avoid = '' if n == 1 else characters[1]
            characters[0] = replacement(avoid)
        
        return ''.join(characters)
