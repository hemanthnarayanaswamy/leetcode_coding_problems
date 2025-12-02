class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        Increasing = True

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1] and Increasing:
                continue
            elif arr[i] < arr[i-1] and i > 1:
                Increasing = False
            else:
                return False
                
        return True and not Increasing