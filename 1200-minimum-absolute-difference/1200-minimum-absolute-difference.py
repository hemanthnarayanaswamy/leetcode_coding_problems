class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        result = []

        for i in range(len(arr)-1):
            a, b = arr[i], arr[i+1]
            tempDiff = abs(b - a)
            
            if tempDiff < minDiff:
                minDiff = tempDiff
                result = [[a, b]]

            elif tempDiff == minDiff:
                 result.append([a, b])
                
        return result 