class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1

        for c in s:
            if c.isdigit():
                d = int(c)
                if d > first:
                    second = first
                    first = d
                elif first > d > second:
                    second = d

        return second