class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())
        deletions = float('inf')

        for f1 in freq:
            base = f1
            tmp = []
            for f2 in freq:
                if f2 < base:
                    tmp.append(f2)
                elif f2 > base and f2 - base > k:
                    tmp.append(f2 - base - k)
                else:
                    tmp.append(0)

            
            if sum(tmp) < deletions:
                deletions = sum(tmp)
        
        return deletions

