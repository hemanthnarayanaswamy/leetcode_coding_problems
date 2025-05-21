class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()

        salarySum = sum(salary[1:n-1])

        return salarySum / (n-2)