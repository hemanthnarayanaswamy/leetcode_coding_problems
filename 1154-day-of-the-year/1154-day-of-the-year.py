class Solution:
    def dayOfYear(self, date: str) -> int:
        days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        y, m, d = map(int,date.split("-"))

        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            days[2] += 1
        
        count = 0

        for i in range(1, m):
            count += days[i]
        
        count += d

        return count
