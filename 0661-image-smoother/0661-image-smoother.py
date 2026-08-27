class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0]*n for _ in range(m)]

        def getAvg(x, y):
            count = total = 0
            for i in range(max(0, x-1), min(x+2, m)):
                for j in range(max(0, y-1), min(y+2, n)):
                    count += 1
                    total += img[i][j]
    
            return total//count
        
        for i in range(m):
            for j in range(n):
                res[i][j] = getAvg(i, j)

        return res