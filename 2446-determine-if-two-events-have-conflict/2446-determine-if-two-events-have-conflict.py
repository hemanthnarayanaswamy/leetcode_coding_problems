class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2

        if start1 > start2:  # if event2 starts before event1 we swap the variables
            start1, start2 = start2, start1
            end1, end2 = end2, end1
        
        return True if end1 >= start2 else False