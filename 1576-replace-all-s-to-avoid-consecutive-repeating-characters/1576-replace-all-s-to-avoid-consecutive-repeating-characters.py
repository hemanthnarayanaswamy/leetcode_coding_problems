class Solution:
    def modifyString(self, s: str) -> str:
        def replacement(pc, nc):
            lower = 'abcdefghijklmnopqrstuvwxyz'
            c = 'a'
            while c == pc or c == nc:
                c = lower[(ord(c) - 97 + 1) % 26]
            return c
        
        characters = list(s)
        n = len(s)

        for i in range(n):
            if characters[i] == '?':
                pc = characters[i - 1] if i > 0 else None
                nc = characters[i + 1] if i < n - 1 else None

                characters[i] = replacement(pc, nc)
        
        return ''.join(characters)
