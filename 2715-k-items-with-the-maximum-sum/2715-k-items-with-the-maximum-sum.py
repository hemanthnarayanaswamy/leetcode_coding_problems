class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        items = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes

        return sum(items[:k])