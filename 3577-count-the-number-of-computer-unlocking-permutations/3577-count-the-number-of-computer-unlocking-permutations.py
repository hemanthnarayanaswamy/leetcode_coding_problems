class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        min_c = complexity[0]
        for i in range(1, n):
            if complexity[i] <= min_c:
                return 0

        fact = 1
        for i in range(1, n):
            fact = (fact * i) % MOD
            
        return fact