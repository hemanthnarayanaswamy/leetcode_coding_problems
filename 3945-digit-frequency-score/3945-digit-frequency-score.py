class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = Counter(str(n))
        score = 0

        for num, f in freq.items():
            score += int(num)*f
        
        return score