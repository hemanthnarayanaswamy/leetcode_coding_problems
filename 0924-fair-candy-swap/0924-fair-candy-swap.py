class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobs = set(bobSizes)
        diff = (sum(bobSizes) - sum(aliceSizes)) // 2

        for a in aliceSizes:
            b = a + diff
            if b in bobs:
                return [a, b]

