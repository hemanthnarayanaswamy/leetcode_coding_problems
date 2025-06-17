class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # sum up 1 for each (s,e) where s <= queryTime <= e
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
