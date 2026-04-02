class Solution:
    def sumBase(self, n: int, k: int) -> int:
        q, r = divmod(n, k)
        res = r

        while q:
            q, r = divmod(q,k)
            res += r
            
        return res
