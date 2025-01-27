class Solution:
    def isMonotonic(self, arr: List[int]) -> bool:
        is_decreasing, is_increasing = True, True
        array_len = len(arr)
        if array_len < 2:
            return True
        for i in range(array_len):
            if i+1 < array_len:
                current_ele, next_ele = arr[i], arr[i+1]
                if current_ele > next_ele:
                    is_decreasing = False
                if current_ele < next_ele:
                    is_increasing = False
                if current_ele == next_ele:
                    is_decreasing, is_increasing = is_decreasing, is_increasing
            if is_decreasing == False and is_increasing == False:
                return False
        return True
        