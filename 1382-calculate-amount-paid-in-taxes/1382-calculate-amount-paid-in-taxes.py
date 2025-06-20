class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        taxAmount = 0.0
        taxAccumulated = 0
        prev = 0

        for i in range(len(brackets)):
            if income <= prev: # Early exit: as soon as your income ≤ the previous bracket’s upper bound, you stop looping.
                break 

            upper, percentage = brackets[i][0], brackets[i][1] / 100
            taxableIncome = min(income, upper) - prev
            
            taxAmount += taxableIncome * percentage 
            prev = upper
        
        return taxAmount 
