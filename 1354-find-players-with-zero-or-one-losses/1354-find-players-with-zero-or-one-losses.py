class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossTracker = {}
        onelose = []
        nolose = []

        # for match in matches:
        #     w, l = match[0], match[1]
        #     lossTracker[l] = lossTracker.get(l, 0) + 1
        #     if w not in lossTracker:
        #         lossTracker[w] = 0
        for w, l in matches:
            lossTracker[l] = lossTracker.get(l, 0) + 1
            if w not in lossTracker:
                lossTracker[w] = 0
        
        #lossTrackerSort = dict(sorted(lossTracker.items(), key=lambda item: item[0]))
        
        for player, lose in lossTracker.items():
            if lose == 0:
                nolose.append(player)
            
            elif lose == 1:
                onelose.append(player)

        nolose.sort()
        onelose.sort()

        return [sorted(nolose), sorted(onelose)]


        