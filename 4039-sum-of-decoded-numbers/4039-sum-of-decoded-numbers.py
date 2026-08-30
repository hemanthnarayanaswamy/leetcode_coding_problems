class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        total = 0
        MOD = 10**9+7

        for num in nums:
            w = num % 10
            d = str(num // 10)
            x, y = int(d[:w]), int(d[w:])
            subtotal = pow(x, y, MOD)
            total = (total + subtotal) % MOD
        
        return total