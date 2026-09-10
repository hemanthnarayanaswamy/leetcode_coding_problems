class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n | k != n:
            return -1

        return bin(n).count('1') - bin(k).count('1')