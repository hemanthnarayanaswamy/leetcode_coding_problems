class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountainPeak = False
        n = len(arr)
        sortedArr = sorted(arr)

        if n < 3:
            return False
        elif sortedArr == arr or sortedArr == arr[::-1]:
            return False

        for i in range(n - 1):
            if arr[i] > arr[i+1]:
                mountainPeak = True 

            if not mountainPeak and arr[i] >= arr[i+1]:
                return False
            elif mountainPeak and arr[i] <= arr[i+1]:
                return False
        
        return True
            
