class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num)
        complementNum = []

        for i in binNum[2::]:
            if i == '1':
                complementNum.append('0')
            else: 
                complementNum.append('1')
        print(complementNum)
        
        return int(''.join(complementNum), 2)
