class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len([empHrs for empHrs in hours if empHrs >= target])