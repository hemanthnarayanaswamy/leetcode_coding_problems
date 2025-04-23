class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        result = n

        if n == k:
            return blocks.count('W')

        for i in range(n-k+1):
            result = min(result, blocks[i:i+k].count('W'))
        
        return result
        