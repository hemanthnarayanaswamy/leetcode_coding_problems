class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 1) Turn “HH:MM” into total minutes
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))
        diff = (h2 * 60 + m2) - (h1 * 60 + m1)

        # 2) Greedily use the largest operations first
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
            if diff == 0:
                break

        return ops