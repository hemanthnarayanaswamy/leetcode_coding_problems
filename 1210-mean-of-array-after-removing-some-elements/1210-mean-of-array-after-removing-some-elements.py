class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        removeElement=n//20 # 5% computation 

        arr = arr[removeElement:-removeElement]

        return sum(arr) / len(arr)
        