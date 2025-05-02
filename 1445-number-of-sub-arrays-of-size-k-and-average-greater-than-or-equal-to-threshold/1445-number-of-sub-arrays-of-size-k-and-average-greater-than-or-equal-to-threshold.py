class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter, i = 0, 0
        initSum = sum(arr[:k])
        thresholdSum = threshold * k

        if initSum >= thresholdSum:
            counter += 1
        
        for j in range(k, len(arr)):
            initSum = initSum + arr[j] - arr[i]
            i += 1

            if initSum >= thresholdSum:
                counter += 1
            
        return counter

            

        