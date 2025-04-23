class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        result = n

        for i in range(n-k+1):
            result = min(result, blocks[i:i+k].count('W'))
        
        return result
        