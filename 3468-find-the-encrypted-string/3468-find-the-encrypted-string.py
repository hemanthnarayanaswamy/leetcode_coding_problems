class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        if n == 0:
            return s
        r = k % n
        out = [''] * n
        for i, ch in enumerate(s):
            out[i] = s[(i + r) % n]
        return ''.join(out)