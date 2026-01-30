class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        n = len(number)
        res = []
        i = 0           
        while i < n:
            if n - i > 4:
                res.append(number[i:i+3])
                i += 3
            elif n - i == 4:
                res.append(number[i:i+2])
                i += 2 
            else:
                res.append(number[i:])
                i = n
        
        return '-'.join(res)
