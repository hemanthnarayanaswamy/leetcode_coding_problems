class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        pre = complexity[0]
        unlocked = 1

        for i in range(1, n):
            if complexity[i] > pre:
                unlocked += 1
                pre = min(pre, complexity[i])
        
        if unlocked == n:
            premutation = 1
            for i in range(1, unlocked):
                premutation *= i
            
            return premutation % (10 ** 9 + 7)
        
        return 0