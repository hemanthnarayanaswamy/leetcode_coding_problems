class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = [1]
        ans = 0

        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                groups.append(1)
            else:
                groups[-1] += 1
        
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1])
        
        return ans
        