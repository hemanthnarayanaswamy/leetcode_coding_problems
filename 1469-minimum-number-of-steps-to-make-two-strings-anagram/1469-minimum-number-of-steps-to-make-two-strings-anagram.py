

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_feq, t_feq = {}, {} 
        for i in range(len(s)):
            s_feq[s[i]] = s_feq.get(s[i], 0) + 1
            t_feq[t[i]] = t_feq.get(t[i], 0) + 1


        count = 0           # To track the Changes Required

        for char in t_feq:  # Check each char in t
            if char not in s_feq:   # If that char is not in s
                count += t_feq[char]  # All that char needs to be changed
            else:
                temp_diff = t_feq[char] - s_feq[char]
                if temp_diff > 0:  # If that element is present and If its count is excess than s 
                    count += temp_diff  # it also needs to be changed
        return count

        