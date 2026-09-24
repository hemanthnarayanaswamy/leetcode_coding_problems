class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        total = chunk = 0 
        actualSum = [0]

        for i in range(1, len(arr)):
            actualSum.append(actualSum[i-1] + i)


        for i, num in enumerate(arr):
            total += num 

            if actualSum[i] == total:
                chunk += 1
        
        return chunk