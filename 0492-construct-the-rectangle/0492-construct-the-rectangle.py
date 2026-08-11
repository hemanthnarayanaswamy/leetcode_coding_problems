class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L, W = area, 1
        
        for i in range(int(area ** 0.5), 0, -1):
            if area % i:
                continue

            w = i 
            l = area // i

            if abs(l - w) < abs(L - W):
                L = l
                W = w
        
        return [L, W]