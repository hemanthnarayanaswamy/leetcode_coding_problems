class Solution:
    def minimizedStringLength(self, s: str) -> int:
        Uniq = set()
        count = 0

        for char in s:
            if char not in Uniq:
                count += 1
                Uniq.add(char)

        return count
