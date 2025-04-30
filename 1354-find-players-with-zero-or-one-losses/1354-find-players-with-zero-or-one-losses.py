class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossTracker = {}
        onelose = []
        nolose = []

        for match in matches:
            w, l = match[0], match[1]
            lossTracker[w] = lossTracker.get(w, 0) + 0
            lossTracker[l] = lossTracker.get(l, 0) + 1
        
        lossTrackerSort = dict(sorted(lossTracker.items(), key=lambda item: item[0]))
        
        for player, lose in lossTrackerSort.items():
            if lose == 0:
                nolose.append(player)
            
            elif lose == 1:
                onelose.append(player)
        
        return [nolose, onelose]


        