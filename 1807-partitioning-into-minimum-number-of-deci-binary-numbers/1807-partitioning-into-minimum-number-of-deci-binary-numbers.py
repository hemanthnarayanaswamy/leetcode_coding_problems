class Solution:
    def minPartitions(self, n: str) -> int:
        n_int = [int(num) for num in n]
        return max(n_int)