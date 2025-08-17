class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keyMap = {keysPressed[0]:releaseTimes[0]}

        for i in range(1, len(keysPressed)):
            tmp = releaseTimes[i] - releaseTimes[i-1]
            c = keysPressed[i]
            
            if c in keyMap:
                if keyMap[c] < tmp:
                    keyMap[c] = tmp
            else:
                keyMap[c] = tmp
        
        res, val = 0, 0

        for c, v in keyMap.items():
            if v > val:
                val = v
                res = c
            elif v == val:
                if c > res:
                    val = v
                    res = c
        
        return res

