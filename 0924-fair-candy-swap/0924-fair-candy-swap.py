class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        bobs = set(bobSizes)
        diff = (sumB - sumA) // 2

        for a in aliceSizes:
            b = a + diff
            if b in bobs:
                return [a, b]

