class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1,i1 = map(int, num1[:-1].split('+'))
        r2,i2 = map(int, num2[:-1].split('+'))
        
        return str(r1*r2 - i1*i2) + "+" + str(r1*i2 + r2*i1) + 'i' 
        