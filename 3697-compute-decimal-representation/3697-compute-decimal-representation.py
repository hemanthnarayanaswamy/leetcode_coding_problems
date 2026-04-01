class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        res = []
        factor = 1

        while n:
            d, r = divmod(n, 10)
            if r:
                res.append(r * factor)
            n = d
            factor *= 10

        return res[::-1]
