class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)[2:]
        complementNum = []

        for i in binNum:
            complementNum.append('0') if i == '1' else complementNum.append('1')
        
        return int(''.join(complementNum), 2)
