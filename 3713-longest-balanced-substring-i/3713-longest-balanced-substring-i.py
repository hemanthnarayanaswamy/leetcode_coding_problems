class Solution:
    def longestBalanced(self, s: str) -> int:
        longest = 0
        n = len(s)

        for i in range(n):
            freq = Counter()
            countFreq = Counter()
            for j in range(i, n):
                c = s[j]
                old = freq[c]

                if old > 0:
                    countFreq[old] -= 1

                    if countFreq[old] == 0:
                        del countFreq[old]

                freq[c] += 1
                countFreq[freq[s[j]]] += 1
        
                if len(countFreq) == 1:
                    longest = max(longest, j - i + 1)
        
        return longest
