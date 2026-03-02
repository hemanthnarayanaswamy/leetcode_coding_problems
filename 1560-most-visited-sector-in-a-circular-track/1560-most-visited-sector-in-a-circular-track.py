class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        trackVisit = [0] * n
        start = rounds[0]
        i = 1

        while i < len(rounds):
            end = rounds[i]
            if end < start:
                end += n

            for j in range(start-1, end):
                trackVisit[j%n] += 1
            start = (rounds[i] + 1) % n
            i += 1
        
        maxVisits = max(trackVisit)

        return [i+1 for i in range(len(trackVisit)) if trackVisit[i] == maxVisits]