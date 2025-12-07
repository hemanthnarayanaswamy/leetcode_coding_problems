class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sn = len(s)
        gn = len(goal)
        sfreq = Counter(s)
        gfreq = Counter(goal)

        if (sn != gn) or (sfreq != gfreq):
            return False
        
        if s == goal:
            for v in sfreq.values():
                if v >= 2:
                    return True
            return False
        
        misMatch = 0
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                misMatch += 1
            
            if misMatch > 2:
                return False
        
        return True
