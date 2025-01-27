class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        is_decreasing, is_increasing = True, True
        array_len = len(arr)
        for i in range(array_len):
            if i+1 < array_len:
                if arr[i] > arr[i+1]:
                    is_decreasing = False
                if arr[i] < arr[i+1]:
                    is_increasing = False
                if arr[i] == arr[i+1]:
                    is_decreasing, is_increasing = is_decreasing, is_increasing
            print(is_decreasing, is_increasing)
            if is_decreasing == False and is_increasing == False:
                return False
        return True
        