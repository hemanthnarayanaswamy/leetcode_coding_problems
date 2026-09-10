class Solution:
    def minChanges(self, n: int, k: int) -> int:
        res = 0
        if n == k:
            return res
        
        if n | k != n:
            return -1

        print(bin(n), bin(k))
        return bin(n).count('1') - bin(k).count('1')