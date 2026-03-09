class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0

        if x <= 3:
            return 1

        l, r = 2, x//2

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            print(l, r, mid)

            if square == x:
                return mid
            elif square > x:
                r = mid - 1
            else:
                l = mid + 1

        return (l+r)//2