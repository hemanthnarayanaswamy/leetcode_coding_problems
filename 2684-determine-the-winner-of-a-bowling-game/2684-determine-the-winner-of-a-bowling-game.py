class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        i = 0
        s1 = s2 = 0
        p1_multiplier = 0
        p2_multiplier = 0

        while i < len(player1):
            p1 = player1[i]
            p2 = player2[i]

            if p1_multiplier:
                s1 += player1[i]*2
                p1_multiplier -= 1
            else:
                s1 += player1[i]
            
            if p2_multiplier:
                s2 += player2[i]*2
                p2_multiplier -= 1
            else:
                s2 += player2[i]

            if p1 == 10:
                p1_multiplier = 2
            if p2 == 10:
                p2_multiplier = 2
            
            i += 1
        
        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        else:
            return 0
