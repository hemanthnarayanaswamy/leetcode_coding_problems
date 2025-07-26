class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        maxKind = max(Counter(ranks).values())

        if maxKind > 2:
            return "Three of a Kind"
        elif maxKind > 1:
            return "Pair"
        else:
            return "High Card"



        
        
        