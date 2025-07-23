class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        idx = 0
        give = 1
        
        # keep giving until we run out
        while candies > 0:
            # give either `give` or whatever's left
            take = min(give, candies)
            res[idx] += take
            
            # update for next round
            candies -= take
            give     += 1
            idx      = (idx + 1) % num_people
        
        return res