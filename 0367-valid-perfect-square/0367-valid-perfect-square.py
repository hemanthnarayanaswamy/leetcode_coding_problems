class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num 

        while l <= r:
            mid = (l + r) // 2
            square = mid ** 2
            print(l, r)
            print(mid, square)

            if square == num:
                return True
            elif square > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False