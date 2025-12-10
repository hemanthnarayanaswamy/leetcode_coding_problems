class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        root = complexity[0]

        for i in range(1, n):
            if complexity[i] <= root:
                return 0

        premutation = 1
        for i in range(1, n):
            premutation *= i
            premutation %= (10**9 + 7)
        
        return premutation
