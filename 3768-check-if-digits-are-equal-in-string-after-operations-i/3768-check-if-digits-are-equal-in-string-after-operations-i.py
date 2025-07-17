class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # map characters → integers
        digits = list(map(int, s))
        # repeatedly replace with pairwise sums mod 10
        while len(digits) > 2:
            # zip(digits, digits[1:]) walks through pairs (a, b)
            digits = [(a + b) % 10 for a, b in zip(digits, digits[1:])]

        return digits[0] == digits[1]
