class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        unq_subs = 0

        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                unq_subs += 1
        
        return unq_subs
        