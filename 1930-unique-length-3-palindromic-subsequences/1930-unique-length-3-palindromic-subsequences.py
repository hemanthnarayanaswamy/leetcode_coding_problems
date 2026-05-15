class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        count = 0
        first_idx = {}
        last_idx = {}

        for i, c in enumerate(s):
            if c not in first_idx:
                first_idx[c] = i
        
        for j in range(len(s)-1, -1, -1):
            c = s[j]
            if c not in last_idx:
                last_idx[c] = j
        
        for letter in letters:
            i = first_idx.get(letter, -1)
            j = last_idx.get(letter, -1)

            if i == -1 or j == -1 or i == j:
                continue
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            count += len(between)

        return count