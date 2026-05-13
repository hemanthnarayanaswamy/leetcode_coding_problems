class Solution:
    def captureForts(self, forts: List[int]) -> int:
        maxCaptured = 0

        for i in range(len(forts)):
            if forts[i] == 1:
                captured = 0
                for j in range(i+1, len(forts)):
                    if forts[j] == 0:
                        captured += 1
                    elif forts[j] == -1:
                        maxCaptured = max(captured, maxCaptured)
                        break
                    else:
                        break
                    
        for i in range(len(forts)-1, -1, -1):
            if forts[i] == 1:
                captured = 0
                for j in range(i-1, -1, -1):
                    if forts[j] == 0:
                        captured += 1
                    elif forts[j] == -1:
                        maxCaptured = max(captured, maxCaptured)
                        break
                    else:
                        break
        
        return maxCaptured