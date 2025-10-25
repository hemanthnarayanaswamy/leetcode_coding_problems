class Solution:
    def totalMoney(self, n: int) -> int:
        startMoney = 1
        money = 1
        dayOfWeek = 0
        totalMoney = 0
        totalDays = 0

        while totalDays < n:
            totalMoney += money
            dayOfWeek += 1
            totalDays += 1
            money += 1

            if dayOfWeek == 7:
                dayOfWeek = 0
                startMoney += 1
                money = startMoney
        
        return totalMoney





