class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        peak = arr.index(max(arr))

        # Peak cannot be at edges
        if peak == 0 or peak == n - 1:
            return False

        # Check strictly increasing
        for i in range(peak):
            if arr[i] >= arr[i + 1]:
                return False

        # Check strictly decreasing
        for i in range(peak, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True