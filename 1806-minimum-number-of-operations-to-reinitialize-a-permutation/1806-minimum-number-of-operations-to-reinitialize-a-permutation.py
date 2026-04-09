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

        operations = 0
        perm = [i for i in range(n)]
        initial = perm

        for i in range(n):
            perm = specialOperation(perm)
            operations += 1

            if perm == initial:
                break
        
        return operations

        


