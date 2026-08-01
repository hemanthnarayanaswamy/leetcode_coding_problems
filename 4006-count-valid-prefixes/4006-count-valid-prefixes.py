class Solution:
    def countValidPrefixes(self, s: str) -> int:
        freq = defaultdict(int)
        pre = 0

        for c in s:
            freq[c] += 1

            if abs(freq['1'] - freq['0']) <= 1:
                pre += 1
        
        return pre