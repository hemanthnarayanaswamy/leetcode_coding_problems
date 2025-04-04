from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        s_freq = Counter(s)
        count = 0

        for k,v in s_freq.items():
            if v >= 3:
                if v % 2 == 0:
                    count += 2
                else:
                    count += 1
            else:
                count += v
            
        return count
        