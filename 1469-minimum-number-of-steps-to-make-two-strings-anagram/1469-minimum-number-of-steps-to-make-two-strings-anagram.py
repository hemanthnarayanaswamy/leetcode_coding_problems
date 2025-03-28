from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_feq = Counter(s)  ## Compute the Frequency of the elements 
        t_feq = Counter(t)

        count = 0           # To track the Changes Required

        for char in t_feq:  # Check each char in t
            if char not in s_feq:   # If that char is not in s
                count += t_feq[char]  # All that char needs to be changed
            else:
                temp_diff = t_feq[char] - s_feq[char]
                if temp_diff > 0:  # If that element is present and If its count is excess than s 
                    count += temp_diff  # it also needs to be changed
        return count

        