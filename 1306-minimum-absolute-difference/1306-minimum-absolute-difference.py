class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        result = []

        for i in range(len(arr)-1):
            minDiff = min(minDiff,abs(arr[i]-arr[i+1]))
            if minDiff == 1:
                break

        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1]
        
            if  abs(b - a) == minDiff:
                 result.append([a, b])
                
        return result 

