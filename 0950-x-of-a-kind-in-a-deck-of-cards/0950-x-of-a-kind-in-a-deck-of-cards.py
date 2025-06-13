import math 

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        cardCounts = [v for v in Counter(deck).values()]

        Xgcd = math.gcd(*cardCounts)

        return Xgcd != 1