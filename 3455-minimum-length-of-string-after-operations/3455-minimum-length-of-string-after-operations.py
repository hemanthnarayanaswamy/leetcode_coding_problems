class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0
        for char in set(s):
            if s.count(char) % 2:
                count += 1
            else:
                count += 2
        return count