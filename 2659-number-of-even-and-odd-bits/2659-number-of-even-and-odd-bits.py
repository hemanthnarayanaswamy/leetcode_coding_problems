class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binN = bin(n)[2::][::-1]
        res = [0, 0]

        for i in range(len(binN)):
            if binN[i] == '1':
                if i % 2:
                   res[1] += 1
                else:
                    res[0] += 1
        
        return res