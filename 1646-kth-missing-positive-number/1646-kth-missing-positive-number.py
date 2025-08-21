class Solution:
    def findKthPositive(self, arr, k):
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2 
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid 
        return r + k

