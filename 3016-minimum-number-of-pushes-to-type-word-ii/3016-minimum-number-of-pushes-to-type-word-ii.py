class Solution:
    def minimumPushes(self, word: str) -> int: 
        freq = sorted(Counter(word).values(), reverse = True)
        totalPushes = 0

        for i, f in enumerate(freq):
            totalPushes += f * (i // 8 + 1)

        return totalPushes