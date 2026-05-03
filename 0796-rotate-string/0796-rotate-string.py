class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Quick length check
        if len(s) != len(goal):
            return False
        
        # Double s and see if goal sits inside
        return goal in (s + s)