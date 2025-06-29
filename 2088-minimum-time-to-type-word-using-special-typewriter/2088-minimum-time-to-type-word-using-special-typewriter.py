class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        last = 'a'

        for curr in word:
            diff = abs(ord(curr) - ord(last))
            time += min(diff, 26 - diff) + 1
            last = curr

        return time