class Solution:
    def reinitializePermutation(self, n: int) -> int:
        def specialOperation(perm):
            n = len(perm)
            arr = []
            for i in range(len(perm)):
                if i % 2:
                    arr.append(perm[n // 2 + (i - 1) // 2]) 
                else:
                    arr.append(perm[i//2])
            return arr

        initial = [i for i in range(n)]
        perm = initial

        for i in range(1, n):
            perm = specialOperation(perm)

            if perm == initial:
                break
        
        return i