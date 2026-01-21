class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k == 1:
            return s
        elif k == len(s):
            return s[::-1]
        else:
            return s[:k][::-1] + s[k:]