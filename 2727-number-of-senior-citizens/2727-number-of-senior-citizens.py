class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniorCount = 0

        for detail in details:
            if int(detail[-4:-2]) > 60:
                seniorCount += 1
        
        return seniorCount
    