class Solution:
    def totalMoney(self, n: int) -> int:
        fullWeeks = n // 7
        leftDays = n % 7
        totalMoney = 0

        for i in range(fullWeeks): # Using AP to calculate the amount for the fullweeks
            totalMoney += 7 * (1 + i) + 21
        
        # calculate amount for remaining weeks
        f = 1+fullWeeks
        l = f+leftDays-1 

        totalMoney += leftDays * (f + l)//2
        
        return totalMoney
        