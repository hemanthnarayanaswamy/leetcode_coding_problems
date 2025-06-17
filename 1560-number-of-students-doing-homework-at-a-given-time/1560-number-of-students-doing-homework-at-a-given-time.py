class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0

        for t1,t2 in zip(startTime, endTime):
            if queryTime in range(t1, t2+1):
                result += 1
        
        return result
