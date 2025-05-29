class Solution:
    def numberOfMatches(self, n: int) -> int:
        res, teams = 0, n
        while teams > 1:
            res += teams // 2
            teams = teams // 2 + teams % 2

        return res