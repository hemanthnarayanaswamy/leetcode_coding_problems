class Solution:
    def minDeletions(self, s: str) -> int:
        arr = sorted(Counter(s).values(), reverse=True)
        freq_val = Counter(arr)
        n = len(arr)
        count = 0
        
        if n == len(set(arr)):
            return count

        for f in arr:
            while f > 0 and freq_val[f] > 1:
                count += 1
                freq_val[f] -= 1
                f -= 1
                freq_val[f] += 1
        
        return count