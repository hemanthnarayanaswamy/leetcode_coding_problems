class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        minNum, maxNum = salary[0], salary[0]

        for income in salary:
            if income < minNum:
                minNum = income
            
            if income > maxNum:
                maxNum = income 
        
        return (sum(salary) - maxNum - minNum) / (n-2)