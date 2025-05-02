class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        initSum = sum(arr[:k])
        thresholdSum = threshold * k

        if initSum >= thresholdSum:
            counter += 1
        
        for i in range(k, len(arr)):
            initSum = initSum + arr[i] - arr[i-k]
            i += 1

            if initSum >= thresholdSum:
                counter += 1
            
        return counter

            

        