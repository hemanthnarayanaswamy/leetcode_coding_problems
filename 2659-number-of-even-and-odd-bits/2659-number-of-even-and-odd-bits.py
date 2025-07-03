class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binN = bin(n)[2::][::-1]
        e, o = 0, 0

        for i in range(len(binN)):
            if binN[i] == '1':
                if i % 2:
                    o += 1
                else:
                    e += 1
        
        return [e, o]