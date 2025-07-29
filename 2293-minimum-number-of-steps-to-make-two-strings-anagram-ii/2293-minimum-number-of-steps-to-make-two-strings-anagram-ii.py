class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        counter_s = Counter(s)
        counter_t = Counter(t)
        chars = "qwertyuiopasdfghjklzxcvbnm"

        for char in chars:
            res += abs(counter_s[char] - counter_t[char])
        return res