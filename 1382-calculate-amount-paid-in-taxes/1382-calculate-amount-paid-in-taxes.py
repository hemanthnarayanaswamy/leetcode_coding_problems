class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax  = 0
        prev = 0

        for upper, pct in brackets:
            if income <= prev:
                break

            # how much of your income falls in this bracket
            taxable = min(income, upper) - prev
            tax    += taxable * (pct / 100)
            prev    = upper

        return tax
