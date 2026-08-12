class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        pattern = "(" * k + ")" * k
        while pattern in s:
            s = s.replace(pattern, "")
        return s