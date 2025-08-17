class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res, val = keysPressed[0], releaseTimes[0]

        for i in range(1, len(keysPressed)):
            tmp = releaseTimes[i] - releaseTimes[i-1]
            c = keysPressed[i]

            if tmp > val:
                val = tmp
                res = c
            elif tmp == val:
                if c > res:
                    val = tmp
                    res = c
        
        return res