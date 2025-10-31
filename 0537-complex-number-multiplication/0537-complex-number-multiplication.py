class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a = b = c = d = 0
    
        i = num1.index('+')
        j = num2.index('+')
        
        a = int(num1[:i])
        b = int(num1[i+1:-1]) # Ignore the i
        c = int(num2[:j])
        d = int(num2[j+1:-1])
        print(a, b, c, d)

        return str(a*c - b*d) + '+' + str(a*d + b*c) + 'i'
