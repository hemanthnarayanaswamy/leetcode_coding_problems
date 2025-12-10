class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        pre = complexity[0]
        unlocked = 1

        for i in range(1, n):
            if complexity[i] > pre:
                unlocked += 1
            else:
                return 0
        
        premutation = 1
        for i in range(1, n):
            premutation *= i
            premutation %= (10**9 + 7)
        
        return premutation
