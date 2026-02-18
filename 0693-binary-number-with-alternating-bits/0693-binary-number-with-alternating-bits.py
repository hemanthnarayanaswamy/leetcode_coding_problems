class Solution(object):
    def hasAlternatingBits(self, n):
        binaryVal = bin(n)
        return False if '00' in binaryVal or '11' in binaryVal else True
        