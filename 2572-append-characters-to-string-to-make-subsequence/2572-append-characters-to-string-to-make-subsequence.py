class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not t:
            return 0
        ti = 0
        for c in s:
            if c == t[ti]:
                ti += 1
                if ti == len(t):
                    return 0
        return len(t) - ti