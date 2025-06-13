class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        arr = [num%2 for num in arr]

        for i in range(len(arr)-2):
            if sum(arr[i:i+3]) == 3:
                return True 
        
        return False