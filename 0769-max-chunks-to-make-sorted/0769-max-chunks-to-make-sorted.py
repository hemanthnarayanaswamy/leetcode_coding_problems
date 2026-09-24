class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        total = chunk = 0 

        for i, num in enumerate(arr):
            total += num 

            if i * (i+1) // 2 == total:
                chunk += 1
        
        return chunk