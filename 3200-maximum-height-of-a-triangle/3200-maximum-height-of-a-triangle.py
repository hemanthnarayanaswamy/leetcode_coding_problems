class Solution:
    def getHeight(self, first: int, second: int) -> int:
            total = first+second+1
            r = b = 0
            for i in range(1, total):
                if i % 2:
                    r += i
                else:
                    b += i
                
                if r > first or b > second:
                    break
            return i - 1

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.getHeight(red, blue), self.getHeight(blue, red))
