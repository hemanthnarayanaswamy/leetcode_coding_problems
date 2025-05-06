class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()

        removeElement = int(0.05 * n)

        arrSum = sum(arr[removeElement:n-removeElement])

        return arrSum / (n - 2*removeElement)
        