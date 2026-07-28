class Solution:
    def smallestPalindrome(self, s: str) -> str:
        partition = len(s) // 2

        base = sorted(s[:partition])
        mid = [s[partition]] if len(s) % 2 == 1 else []

        return "".join(base + mid + base[::-1])