class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        total = red+blue+1
        
        def getHeight(first, second):
            r = b = 0
            for i in range(1, total):
                if i % 2:
                    r += i
                else:
                    b += i
                
                if r > first or b > second:
                    break
            return i - 1
        
        return max(getHeight(red, blue), getHeight(blue, red))
