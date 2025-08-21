class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nextNum = 1

        for num in arr:
            while num != nextNum:
                if k == 1:
                    return nextNum
                nextNum += 1
                k -= 1
            nextNum += 1
        
        return nextNum + k - 1