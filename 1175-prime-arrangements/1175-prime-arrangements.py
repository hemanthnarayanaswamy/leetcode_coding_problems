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
        
        def fact(num):
            answer = 1
            for i in range(2, num+1):
                answer = (answer * i) % mod
            return answer

        primeCount = 0
        for i in range(1, n+1):
            if isprime(i):
                primeCount += 1
        
        nonPrimeCount = n - primeCount

        return (fact(primeCount) * fact(nonPrimeCount)) % mod
        