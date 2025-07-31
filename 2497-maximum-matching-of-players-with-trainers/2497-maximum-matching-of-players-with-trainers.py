class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p, n = 0, len(players)

        for trainer in trainers:
            if trainer >= players[p]:
                p += 1
                if p == n: break
                
        return p