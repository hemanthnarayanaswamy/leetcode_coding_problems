class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        playersPicks = defaultdict(Counter)
        playersWon = 0

        for player, ball in pick:
            playersPicks[player][ball] += 1

        for i in range(n):
            for count in playersPicks[i].values():
                if count > i:
                    playersWon += 1
                    break
                    
        return playersWon
