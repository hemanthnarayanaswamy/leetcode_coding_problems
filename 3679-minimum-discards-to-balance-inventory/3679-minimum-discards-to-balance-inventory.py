class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        inventory = defaultdict(int)
        start = 0
        discardIdx = set()

        for curr, item in enumerate(arrivals):
            if curr - start + 1 > w:
                if start not in discardIdx:
                    inventory[arrivals[start]] -= 1
                start += 1 
            
            if inventory[item] + 1 > m:
                discardIdx.add(curr)
            else:
                inventory[item] += 1
        
        return len(discardIdx)


