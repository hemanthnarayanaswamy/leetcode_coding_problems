class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lm = low % 2
        hm = high % 2
        count = (high - low) // 2

        if lm == 0 and hm == 0:
            return count
        else:
            return count + 1
        