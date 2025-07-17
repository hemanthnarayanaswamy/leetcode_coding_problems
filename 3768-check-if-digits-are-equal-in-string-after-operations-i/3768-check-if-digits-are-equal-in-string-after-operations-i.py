class Solution:
    def hasSameDigits(self, s: str) -> bool:
        t = list(map(int, s))
        while len(t) > 2:
            for i in range(len(t) - 1):
                t[i] = (t[i] + t[i + 1]) % 10
            t.pop()
        return t[0] == t[1]

        