class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binaryVal = bin(n)

        return False if '00' in binaryVal or '11' in binaryVal else True
        