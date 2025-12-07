class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sn = len(s)
        gn = len(goal)
        sfreq = Counter(s)
        gfreq = Counter(goal)

        if sn != gn:
            return False
        elif sfreq != gfreq:
            return False
        
        swap = 2
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                swap -= 1
            
            if swap < 0:
                return False
        
        if swap == 0:
            return True
        
        if sfreq == gfreq:
            for v in sfreq.values():
                if v >= 2:
                    return True
        
        return False
