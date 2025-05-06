class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        n=n//20 # 5% computation 

        arr = arr[n:-n]

        return sum(arr) / len(arr)
        