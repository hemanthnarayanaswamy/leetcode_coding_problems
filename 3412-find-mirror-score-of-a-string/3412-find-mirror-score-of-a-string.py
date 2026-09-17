class Solution:
    def calculateScore(self, s: str) -> int:
        prev = defaultdict(list)
        score = 0

        for i, w in enumerate(s):
            mir = chr(ord('z')-ord(w)+97)

            if mir in prev and prev[mir]:
                j = prev[mir].pop()
                score += i - j
            else:
                prev[w].append(i)

        return score