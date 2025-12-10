class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        root = complexity[0]

        for i in range(1, n):
            if complexity[i] <= root:
                return 0

        return factorial(n-1) % (10**9 + 7)
