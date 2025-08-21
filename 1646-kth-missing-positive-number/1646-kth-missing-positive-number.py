class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        counter = 1

        while k:
            if  i < len(arr) and arr[i] == counter:
                i += 1
            else:
                k -= 1

            counter += 1
        
        return counter - 1

            
            