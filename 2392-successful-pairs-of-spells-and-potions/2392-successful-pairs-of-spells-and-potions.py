class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        def countFor(spell):
            l, r = 0, n
            while l < r:
                m = (l+r)//2
                if potions[m] * spell >= success:
                    r = m
                else:
                    l = m + 1
            
            return n - l
        
        return [countFor(spell) for spell in spells]