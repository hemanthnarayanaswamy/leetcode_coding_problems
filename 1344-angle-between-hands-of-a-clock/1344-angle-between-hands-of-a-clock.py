class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ha = (hour * 30) + (0.5 * minutes)
        ma = minutes * 6

        res = abs(ha - ma)

        return min(res, 360-res)