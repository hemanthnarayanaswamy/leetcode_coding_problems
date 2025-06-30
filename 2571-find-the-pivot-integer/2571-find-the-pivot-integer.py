import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        S = n * (n + 1) // 2
        i = math.isqrt(S)           # integer square root of S
        return i if i * i == S else -1