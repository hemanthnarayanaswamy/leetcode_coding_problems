class Solution:
    def calculateScore(self, s: str) -> int:
        prev = defaultdict(list)
        score = 0

        for i, w in enumerate(s):
            # chr(ord('z')-ord(w)+97)
            mir = chr(219 - ord(w))

            if mir in prev and prev[mir]:
                j = prev[mir].pop()
                score += i - j
            else:
                prev[w].append(i)

        return score