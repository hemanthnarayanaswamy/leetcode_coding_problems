class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalPoints = sum(cardPoints)
        n = len(cardPoints)

        if k == n:
            return totalPoints

        windowSize = n - k
        subTotal = sum(cardPoints[:windowSize])
        maxTotal = totalPoints - subTotal

        left = 0
        for right in range(windowSize, n):
            subTotal = subTotal - cardPoints[left] + cardPoints[right]
            left += 1
            maxTotal = max(maxTotal, totalPoints - subTotal)

        return maxTotal