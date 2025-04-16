class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        unq_subs = 0
        n = len(s)

        if n < 3:
            return unq_subs

        for i in range(n-2):
            if len(set(s[i : i+3])) == 3:
                unq_subs += 1
        
        return unq_subs
