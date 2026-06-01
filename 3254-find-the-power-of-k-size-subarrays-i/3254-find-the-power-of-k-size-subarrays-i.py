class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def checkSequence(arr):
            maxNum = arr[0]
            for i in range(1, len(arr)):
                if arr[i-1] == arr[i]-1:
                    maxNum = max(maxNum, arr[i])
                else:
                    return -1
            return maxNum
        
        res = []
        n = len(nums)

        for i in range(n-k+1):
            tmp = nums[i:i+k]
            res.append(checkSequence(tmp))
        
        return res
            