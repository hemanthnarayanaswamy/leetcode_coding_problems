class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = defaultdict(set)
        res = [0] * k

        for id, t in logs:
            uam[id].add(t)
        
        for time in uam.values():
            res[len(time)-1] += 1
        
        return res