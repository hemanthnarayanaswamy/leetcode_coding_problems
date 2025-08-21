class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        counter = 1
        res = []

        while len(res) < k:
            if  i < len(arr) and arr[i] == counter:
                i += 1
            else:
                res.append(counter)
            counter += 1
        
        return res[k-1]
            