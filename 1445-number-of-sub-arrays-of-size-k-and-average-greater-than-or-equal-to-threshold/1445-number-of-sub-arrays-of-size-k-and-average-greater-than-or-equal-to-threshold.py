class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter, i = 0, 0
        initSum = sum(arr[i:k])

        if initSum / k >= threshold:
            counter += 1
        

        for j in range(k, len(arr)):
            initSum = initSum + arr[j] - arr[i]

            if initSum / k >= threshold:
                counter += 1
            i += 1
            
        return counter

            

        