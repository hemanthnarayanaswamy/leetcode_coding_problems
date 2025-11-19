class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int: 
        arr2.sort()
        ans=len(arr1)

        for i in arr1:
            l, r = 0, len(arr2)-1

            while l<=r:
                m=(l+r)//2
                diff=abs(arr2[m]-i)

                if diff<=d:
                    ans -= 1
                    break
                if arr2[m] > i:
                    r = m-1
                else:
                    l = m+1

        return ans