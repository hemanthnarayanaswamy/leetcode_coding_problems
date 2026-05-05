class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = (10 ** 9) + 7
        def isprime(num):
            if num <= 1:
                return False

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        p = 0

        for i in range(1, n+1):
            if isprime(i):
                p += 1
        
        np = n - p
        
        def fact(num):
            answer = 1
            for i in range(2, num+1):
                answer = (answer * i) % mod
            return answer
        
        return (fact(p) * fact(np)) % mod
        