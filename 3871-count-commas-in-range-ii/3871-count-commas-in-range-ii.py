class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0

        while n:
            print(n, commas)
            if n < 1000:
                return commas
            elif 1000 <= n <= 999999:
                commas += (n - 999)
                return commas
            elif 10 ** 6 <= n <= 999999999:
                d = (n - 999999)
                commas += (2*d)
                n = 999999
            elif 10 ** 9 <= n <= 999999999999:
                d = (n - 999999999)
                commas += (3*d)
                n = 999999999
            elif 10 ** 12 <= n <=  999999999999999:
                d = (n - 999999999999)
                commas += (4*d)
                n = 999999999999
            else:
                d = (n - 999999999999999)
                commas += 5*d
                n = 999999999999999
        
        return commas
 

        

        
