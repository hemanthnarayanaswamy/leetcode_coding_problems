class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def redFirst():
            r = b = 0
            for i in range(1, 200):
                if i % 2:
                    r += i
                else:
                    b += i
                
                if r > red or b > blue:
                    break
            return i - 1
        
        def blueFirst():
            r = b = 0
            for i in range(1, 200):
                if i % 2:
                    b += i
                else:
                    r += i
                
                if r > red or b > blue:
                    break
                    
            return i - 1
        
        return max(blueFirst(), redFirst())
