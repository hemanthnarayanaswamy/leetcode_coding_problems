class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L, W = area, 1
        
        for i in range(1, int(math.sqrt(area))+1):
            w = i 
            l = area // i

            if l >= w and (l * w) == area and abs(l - w) < abs(L - W):
                L = l
                W = w
        
        return [L, W]