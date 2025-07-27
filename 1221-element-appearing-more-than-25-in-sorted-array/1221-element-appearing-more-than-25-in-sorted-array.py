from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4

        count = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                count += 1
                if count > threshold:
                    return arr[i]
            else:
                count = 1
        
        return arr[0]