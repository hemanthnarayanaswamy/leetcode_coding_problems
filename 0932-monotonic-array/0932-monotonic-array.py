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
                    elif current_ele < next_ele:
                        is_increasing = False
                    elif current_ele == next_ele:
                        is_decreasing, is_increasing = is_decreasing, is_increasing
                if not is_decreasing and not is_increasing:
                    return False
            return True
        