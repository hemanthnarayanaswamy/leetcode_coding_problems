class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        playersPicks = defaultdict(Counter)
        playersWon = set()
        

        for player, ball in pick:
            if player in playersWon:
                continue
                
            playersPicks[player][ball] += 1
            if playersPicks[player][ball] > player:
                playersWon.add(player)

        return len(playersWon)
