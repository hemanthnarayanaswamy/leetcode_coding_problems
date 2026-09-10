class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        x0, y0 = start
        x, y = target

        flag_start = (x0 + y0) % 2 == 0
        flag_finish = (x + y) % 2 == 0

        return flag_start == flag_finish
        