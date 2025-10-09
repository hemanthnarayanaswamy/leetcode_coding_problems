class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
            n = len(potions)
            result = [0] * len(spells)
            potions.sort()
            
            def SearchIdx(spell):
                l = 0
                r = n - 1
                while l < r:
                    m = (l + r) // 2
                    if potions[m] * spell >= success:
                        r = m - 1
                    else:
                        l = m + 1
                
                if r >= 0:
                    if potions[r] * spell >= success:
                        return n - r
                    else:
                        return n - r - 1

                return n
            
            for i in range(len(spells)):
                result[i] = SearchIdx(spells[i])

            return result