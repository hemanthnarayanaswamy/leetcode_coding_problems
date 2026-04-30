class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while stones:
            stones.sort()
            x = stones.pop()
            if not stones:
                return x
            y = stones.pop()

            if x != y:
                stones.append(abs(x-y))
        
        return 0