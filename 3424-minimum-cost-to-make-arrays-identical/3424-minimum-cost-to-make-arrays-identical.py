class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)
        c1 = sum([abs(arr[i] - brr[i]) for i in range(n)])

        if c1 <= k:
            return c1

        arr.sort()
        brr.sort()
        c2 = k + sum([abs(arr[i] - brr[i]) for i in range(n)])

        return min(c1, c2)