class Solution:
    def maxOperations(self, s: str) -> int:
        ones = [len(i) for i in s.split('0') if i]
        if not ones:
            return 0
        tot = 0
        ans = 0
        # print(ones[:-1])
        for f in ones[:-1]: # Ignore the last 1
            tot += f
            ans += tot
        if s[-1] == '1':
            return ans
        else:
            tot += ones[-1]
            ans += tot

        return ans