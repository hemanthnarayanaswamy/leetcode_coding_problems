class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        freq_val = Counter(freq.values())
        arr_val = sorted(freq.values(), reverse=True)
        count = 0
        n = len(arr_val)

        if n == len(set(arr_val)):
            return count

        for f in arr_val:
            while freq_val[f] > 1:
                count += 1
                freq_val[f] -= 1
                f -= 1
                if f == 0:
                    break
                freq_val[f] += 1
        
        return count
                

            