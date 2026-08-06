class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ways = 0

        for x in range(0, limit+1):
            for y in range(0, limit+1):
                z = n - (x + y)

                if z >= 0 and z <= limit:
                    ways += 1
        
        return ways