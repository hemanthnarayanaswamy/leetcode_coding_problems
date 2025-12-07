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
        
        swap = 2
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                swap -= 1
            
            if swap < 0:
                return False
        
        return True
