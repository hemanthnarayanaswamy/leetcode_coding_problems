class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binNum = bin(n)[2:]
        complementNum = []

        for i in binNum:
            complementNum.append('0') if i == '1' else complementNum.append('1')
        
        return int(''.join(complementNum), 2)

        