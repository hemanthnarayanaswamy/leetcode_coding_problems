class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        total = 0
        MOD = 1000000007

        for num in nums:
            d, w = divmod(num, 10)
            d = str(d)
            x, y = int(d[:w]), int(d[w:])
            subtotal = pow(x, y, MOD)
            total = (total + subtotal) % MOD
        
        return total