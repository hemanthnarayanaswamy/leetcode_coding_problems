class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] == 0:
                arr.pop(r)
                l += 1
                arr.insert(l, 0)
            l += 1
        