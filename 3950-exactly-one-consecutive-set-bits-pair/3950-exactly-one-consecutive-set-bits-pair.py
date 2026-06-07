class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        prev = None
        count = 0

        for b in binary:
            if b == '1' and prev == b:
                count += 1
            prev = b

            if count > 1:
                return False
        
        return count == 1