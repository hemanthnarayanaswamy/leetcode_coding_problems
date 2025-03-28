from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_feq = Counter(s)
        t_feq = Counter(t)
        print(s_feq, t_feq)
        count = 0

        for char in t_feq:
            if char not in s_feq:
                count += t_feq[char]
            else:
                if t_feq[char] - s_feq[char] > 0:
                    count += abs(s_feq[char] - t_feq[char])


        return count

        