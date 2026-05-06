class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = dict(sorted(Counter(word).items(), key=itemgetter(1), reverse=True))
        multiplier = 1
        counter = 0
        totalPushes = 0

        for v in freq.values():
            if counter == 8:
                counter = 0
                multiplier += 1
            
            totalPushes += (multiplier * v)
            counter += 1
        
        return totalPushes
